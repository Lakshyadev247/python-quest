from flask import Blueprint, jsonify, request, g
from app.database import SessionLocal
from app.models.curriculum import Level, World
from app.models.progress import UserProgress, XPTransaction, ChallengeSubmission, QuizAttempt
from app.models.user import User
from app.services.auth_service import auth_required, optional_auth
from app.services.progress_service import get_or_create_progress, verify_and_update_level_completion
from app.services.gamification_service import award_xp

progress_bp = Blueprint("progress", __name__, url_prefix="/api/progress")

@progress_bp.route("", methods=["GET"])
@auth_required
def get_user_progress():
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        total_levels = db.query(Level).count()
        completed_records = db.query(UserProgress).filter(
            UserProgress.user_id == user.id,
            UserProgress.is_level_completed == True
        ).all()
        completed_count = len(completed_records)
        completion_pct = round((completed_count / total_levels * 100), 1) if total_levels > 0 else 0

        # Recent activities (XP transactions and submissions)
        recent_txs = db.query(XPTransaction).filter(
            XPTransaction.user_id == user.id
        ).order_by(XPTransaction.created_at.desc()).limit(5).all()

        current_world = db.query(World).filter(World.id == user.current_world_id).first()
        if not current_world:
            current_world = db.query(World).first()

        current_level = db.query(Level).filter(Level.number == user.current_level_id).first()

        return jsonify({
            "user": user.to_dict(),
            "total_levels": total_levels,
            "completed_levels_count": completed_count,
            "completion_percentage": completion_pct,
            "current_world": current_world.to_dict() if current_world else None,
            "current_level": current_level.to_dict() if current_level else None,
            "recent_activities": [tx.to_dict() for tx in recent_txs]
        }), 200
    finally:
        db.close()

@progress_bp.route("/lesson", methods=["POST"])
@optional_auth
def complete_lesson():
    data = request.get_json() or {}
    level_id = data.get("level_id")
    if not level_id:
        return jsonify({"error": "level_id is required"}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first() if getattr(g, "user_id", None) else None
        level = db.query(Level).filter(Level.id == level_id).first()
        if not level:
            return jsonify({"error": "Level not found"}), 404

        completed_val = data.get("completed", True)
        if not user:
            return jsonify({
                "message": "Lesson status updated",
                "lesson_completed": bool(completed_val),
                "is_guest": True
            }), 200

        prog = get_or_create_progress(db, user.id, level_id)
        prog.lesson_completed = bool(completed_val)
        db.commit()

        # Award 50 XP for completing lesson if true (idempotent)
        awarded = False
        new_xp = user.total_xp
        if prog.lesson_completed:
            awarded, new_xp = award_xp(
                db, user, 50,
                f"lesson_{level_id}",
                f"Completed lesson for Level {level.number}: {level.title}"
            )

        verification = verify_and_update_level_completion(db, user, level_id)

        return jsonify({
            "message": "Lesson status updated",
            "lesson_completed": prog.lesson_completed,
            "xp_awarded": 50 if awarded else 0,
            "total_xp": new_xp,
            "level_status": verification
        }), 200
    finally:
        db.close()

@progress_bp.route("/level/<int:level_id>", methods=["GET"])
@auth_required
def check_level_status(level_id):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first()
        verification = verify_and_update_level_completion(db, user, level_id)
        prog = get_or_create_progress(db, user.id, level_id)
        return jsonify({
            "progress": prog.to_dict(),
            "verification": verification
        }), 200
    finally:
        db.close()
