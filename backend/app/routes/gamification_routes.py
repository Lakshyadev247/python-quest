from flask import Blueprint, jsonify, request, g
from app.database import SessionLocal
from app.models.progress import Achievement, UserAchievement, XPTransaction, UserProgress, QuizAttempt, ChallengeSubmission
from app.models.curriculum import Level, Lesson, QuizQuestion
from app.models.user import User
from app.services.auth_service import auth_required
from app.services.gamification_service import seed_achievements

gamification_bp = Blueprint("gamification", __name__, url_prefix="/api")

@gamification_bp.route("/achievements", methods=["GET"])
@auth_required
def get_achievements():
    db = SessionLocal()
    try:
        seed_achievements(db)
        all_achs = db.query(Achievement).all()
        user_ach_records = db.query(UserAchievement).filter(
            UserAchievement.user_id == g.user_id
        ).all()
        unlocked_map = {ua.achievement_id: ua.unlocked_at.isoformat() for ua in user_ach_records}

        result = []
        for ach in all_achs:
            a_dict = ach.to_dict()
            a_dict["unlocked"] = ach.id in unlocked_map
            a_dict["unlocked_at"] = unlocked_map.get(ach.id)
            result.append(a_dict)

        return jsonify({
            "total": len(all_achs),
            "unlocked_count": len(unlocked_map),
            "achievements": result
        }), 200
    finally:
        db.close()

@gamification_bp.route("/profile", methods=["GET"])
@auth_required
def get_profile():
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        completed_levels = db.query(UserProgress).filter(
            UserProgress.user_id == user.id,
            UserProgress.is_level_completed == True
        ).count()

        total_submissions = db.query(ChallengeSubmission).filter(
            ChallengeSubmission.user_id == user.id
        ).count()

        passed_submissions = db.query(ChallengeSubmission).filter(
            ChallengeSubmission.user_id == user.id,
            ChallengeSubmission.passed == True
        ).count()

        user_achs = db.query(UserAchievement).filter(
            UserAchievement.user_id == user.id
        ).all()

        recent_txs = db.query(XPTransaction).filter(
            XPTransaction.user_id == user.id
        ).order_by(XPTransaction.created_at.desc()).limit(10).all()

        return jsonify({
            "user": user.to_dict(),
            "stats": {
                "completed_levels": completed_levels,
                "total_submissions": total_submissions,
                "passed_submissions": passed_submissions,
                "unlocked_achievements": len(user_achs)
            },
            "achievements": [ua.to_dict() for ua in user_achs],
            "recent_xp": [tx.to_dict() for tx in recent_txs]
        }), 200
    finally:
        db.close()

@gamification_bp.route("/revision", methods=["GET"])
@auth_required
def get_revision():
    db = SessionLocal()
    try:
        completed_progs = db.query(UserProgress).filter(
            UserProgress.user_id == g.user_id,
            UserProgress.is_level_completed == True
        ).all()

        completed_level_ids = [p.level_id for p in completed_progs]
        levels = db.query(Level).filter(Level.id.in_(completed_level_ids)).order_by(Level.number).all() if completed_level_ids else []

        attempts = db.query(QuizAttempt).filter(
            QuizAttempt.user_id == g.user_id
        ).order_by(QuizAttempt.created_at.desc()).all()

        weak_levels_ids = list({a.level_id for a in attempts if a.score_percent < 100.0})
        weak_levels = db.query(Level).filter(Level.id.in_(weak_levels_ids)).all() if weak_levels_ids else []

        return jsonify({
            "revisable_levels": [lvl.to_dict() for lvl in levels],
            "weak_levels": [lvl.to_dict() for lvl in weak_levels],
            "recent_quiz_attempts": [a.to_dict() for a in attempts[:5]]
        }), 200
    finally:
        db.close()
