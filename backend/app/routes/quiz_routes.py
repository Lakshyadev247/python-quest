import json
from flask import Blueprint, jsonify, request, g
from app.database import SessionLocal
from app.models.curriculum import Level, QuizQuestion, QuizOption
from app.models.progress import QuizAttempt
from app.models.user import User
from app.services.auth_service import auth_required, optional_auth
from app.services.progress_service import get_or_create_progress, verify_and_update_level_completion
from app.services.gamification_service import award_xp

quiz_bp = Blueprint("quiz", __name__, url_prefix="/api/quizzes")

@quiz_bp.route("/<int:level_id>", methods=["GET"])
def get_quiz(level_id):
    db = SessionLocal()
    try:
        level = db.query(Level).filter(Level.id == level_id).first()
        if not level:
            return jsonify({"error": "Level not found"}), 404

        questions = db.query(QuizQuestion).filter(
            QuizQuestion.level_id == level_id
        ).order_by(QuizQuestion.order_index).all()

        return jsonify({
            "level_id": level_id,
            "level_title": level.title,
            "total_questions": len(questions),
            "questions": [q.to_dict(include_answers=False) for q in questions]
        }), 200
    finally:
        db.close()

@quiz_bp.route("/<int:level_id>/submit", methods=["POST"])
@optional_auth
def submit_quiz(level_id):
    data = request.get_json() or {}
    user_answers = data.get("answers", {})

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first() if getattr(g, "user_id", None) else None
        level = db.query(Level).filter(Level.id == level_id).first()
        if not level:
            return jsonify({"error": "Level not found"}), 404

        questions = db.query(QuizQuestion).filter(
            QuizQuestion.level_id == level_id
        ).order_by(QuizQuestion.order_index).all()

        if not questions:
            return jsonify({"error": "No quiz questions found for this level"}), 400

        total_questions = len(questions)
        correct_count = 0
        feedback_list = []

        for q in questions:
            correct_option = next((opt for opt in q.options if opt.is_correct), None)
            selected_option_id = user_answers.get(str(q.id)) or user_answers.get(q.id)
            
            selected_option = None
            if selected_option_id is not None:
                selected_option = next((opt for opt in q.options if opt.id == int(selected_option_id)), None)

            is_correct = (selected_option is not None and selected_option.is_correct)
            if is_correct:
                correct_count += 1

            feedback_list.append({
                "question_id": q.id,
                "question": q.question,
                "code_snippet": q.code_snippet,
                "user_selected_option_id": selected_option_id,
                "user_selected_text": selected_option.option_text if selected_option else "Not answered",
                "is_correct": is_correct,
                "correct_option_id": correct_option.id if correct_option else None,
                "correct_option_text": correct_option.option_text if correct_option else "",
                "explanation": q.explanation or (correct_option.explanation if correct_option else ""),
                "selected_option_explanation": selected_option.explanation if selected_option else ""
            })

        score_percent = round((correct_count / total_questions) * 100.0, 1)
        passed = score_percent >= 80.0

        if not user:
            return jsonify({
                "level_id": level_id,
                "score_percent": score_percent,
                "correct_count": correct_count,
                "total_questions": total_questions,
                "passed": passed,
                "feedback": feedback_list,
                "xp_awarded": int((score_percent / 100.0) * 50) if passed else 0,
                "is_guest": True
            }), 200

        # Save Quiz Attempt record
        attempt = QuizAttempt(
            user_id=user.id,
            level_id=level_id,
            score_percent=score_percent,
            total_questions=total_questions,
            correct_count=correct_count,
            passed=passed,
            answers_json=json.dumps(user_answers)
        )
        db.add(attempt)

        prog = get_or_create_progress(db, user.id, level_id)
        if score_percent > prog.mcq_score:
            prog.mcq_score = score_percent
        if passed:
            prog.mcq_passed = True
        db.commit()

        # Award XP: up to 50 XP scaled to score (idempotent per level)
        xp_to_award = int((score_percent / 100.0) * 50)
        awarded = False
        new_xp = user.total_xp
        if passed and xp_to_award > 0:
            awarded, new_xp = award_xp(
                db, user, xp_to_award,
                f"quiz_{level_id}",
                f"Scored {score_percent}% on Level {level.number} MCQ Examination"
            )

        verification = verify_and_update_level_completion(db, user, level_id)

        return jsonify({
            "level_id": level_id,
            "score_percent": score_percent,
            "correct_count": correct_count,
            "total_questions": total_questions,
            "passed": passed,
            "feedback": feedback_list,
            "xp_awarded": xp_to_award if awarded else 0,
            "total_xp": new_xp,
            "level_status": verification
        }), 200
    finally:
        db.close()
