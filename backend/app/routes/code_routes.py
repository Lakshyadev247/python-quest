from flask import Blueprint, jsonify, request, g
from app.config import Config
from app.database import SessionLocal
from app.models.curriculum import CodingChallenge, TestCase, Level
from app.models.progress import ChallengeSubmission
from app.models.user import User
from app.services.auth_service import auth_required, optional_auth
from app.services.executor_service import execute_python_code, run_test_cases
from app.services.progress_service import get_or_create_progress, verify_and_update_level_completion
from app.services.gamification_service import award_xp
from app.services.rate_limit import rate_limit

code_bp = Blueprint("code", __name__, url_prefix="/api")

@code_bp.route("/code/execute", methods=["POST"])
@optional_auth
@rate_limit(limit=30, window=60)
def execute_code():
    data = request.get_json() or {}
    code = data.get("code", "")
    input_data = data.get("input", "")

    if not code:
        return jsonify({"error": "No Python code provided"}), 400
    if not isinstance(code, str) or len(code) > Config.MAX_CODE_LENGTH:
        return jsonify({
            "error": f"Code must be a string under {Config.MAX_CODE_LENGTH} characters."
        }), 413
    if not isinstance(input_data, str):
        return jsonify({"error": "input must be a string"}), 400
    if len(input_data) > Config.MAX_INPUT_LENGTH:
        return jsonify({
            "error": f"Input exceeds the {Config.MAX_INPUT_LENGTH} character limit."
        }), 413

    result = execute_python_code(code, input_data=input_data)
    return jsonify(result), 200

@code_bp.route("/challenges/<int:challenge_id>", methods=["GET"])
def get_challenge(challenge_id):
    db = SessionLocal()
    try:
        challenge = db.query(CodingChallenge).filter(CodingChallenge.id == challenge_id).first()
        if not challenge and challenge_id <= 126:
            challenge = db.query(CodingChallenge).filter(CodingChallenge.id == (challenge_id + 1299)).first()
        if not challenge and 1300 <= challenge_id <= 1425:
            challenge = db.query(CodingChallenge).filter(CodingChallenge.id == (challenge_id - 1299)).first()
        if not challenge:
            return jsonify({"error": "Challenge not found"}), 404
        return jsonify({"challenge": challenge.to_dict(include_solution=False)}), 200
    finally:
        db.close()

@code_bp.route("/code/submit", methods=["POST"])
@optional_auth
@rate_limit(limit=20, window=60)
def submit_challenge():
    data = request.get_json() or {}
    challenge_id = data.get("challenge_id")
    code = data.get("code", "")

    if not challenge_id or not code:
        return jsonify({"error": "challenge_id and code are required"}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first() if getattr(g, "user_id", None) else None
        challenge = db.query(CodingChallenge).filter(CodingChallenge.id == challenge_id).first()
        if not challenge and isinstance(challenge_id, int) and challenge_id <= 126:
            challenge = db.query(CodingChallenge).filter(CodingChallenge.id == (challenge_id + 1299)).first()
        if not challenge and isinstance(challenge_id, int) and 1300 <= challenge_id <= 1425:
            challenge = db.query(CodingChallenge).filter(CodingChallenge.id == (challenge_id - 1299)).first()
        if not challenge:
            return jsonify({"error": "Challenge not found"}), 404

        test_cases = challenge.test_cases
        eval_result = run_test_cases(code, test_cases)

        if not user:
            xp_reward = challenge.xp_reward
            if challenge.is_boss and xp_reward < 150:
                xp_reward = 150
            return jsonify({
                "challenge_id": challenge.id,
                "passed": eval_result["all_passed"],
                "tests_passed": eval_result["tests_passed"],
                "total_tests": eval_result["total_tests"],
                "stdout": eval_result["stdout"],
                "stderr": eval_result["stderr"],
                "test_results": eval_result["test_results"],
                "xp_awarded": xp_reward if eval_result["all_passed"] else 0,
                "is_guest": True
            }), 200

        # Save submission
        submission = ChallengeSubmission(
            user_id=user.id,
            challenge_id=challenge.id,
            submitted_code=code,
            passed=eval_result["all_passed"],
            stdout=eval_result["stdout"],
            stderr=eval_result["stderr"],
            tests_passed=eval_result["tests_passed"],
            total_tests=eval_result["total_tests"]
        )
        db.add(submission)
        db.commit()

        # Update progress and XP if passed
        awarded = False
        new_xp = user.total_xp
        if eval_result["all_passed"]:
            xp_reward = challenge.xp_reward
            if challenge.is_boss and xp_reward < 150:
                xp_reward = 150

            awarded, new_xp = award_xp(
                db, user, xp_reward,
                f"challenge_{challenge.id}",
                f"Passed {'Boss ' if challenge.is_boss else ''}Challenge: {challenge.title}"
            )

        verification = verify_and_update_level_completion(db, user, challenge.level_id)

        return jsonify({
            "challenge_id": challenge.id,
            "passed": eval_result["all_passed"],
            "tests_passed": eval_result["tests_passed"],
            "total_tests": eval_result["total_tests"],
            "test_results": eval_result["test_results"],
            "stdout": eval_result["stdout"],
            "stderr": eval_result["stderr"],
            "xp_awarded": challenge.xp_reward if awarded else 0,
            "total_xp": new_xp,
            "level_status": verification
        }), 200
    finally:
        db.close()
