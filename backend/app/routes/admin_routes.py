from flask import Blueprint, jsonify, request, g
from app.database import SessionLocal
from app.models.curriculum import World, Level, Lesson, CodingChallenge, TestCase, QuizQuestion, QuizOption
from app.services.auth_service import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

@admin_bp.route("/stats", methods=["GET"])
@admin_required
def get_admin_stats():
    db = SessionLocal()
    try:
        worlds_count = db.query(World).count()
        levels_count = db.query(Level).count()
        lessons_count = db.query(Lesson).count()
        challenges_count = db.query(CodingChallenge).count()
        quizzes_count = db.query(QuizQuestion).count()
        return jsonify({
            "worlds": worlds_count,
            "levels": levels_count,
            "lessons": lessons_count,
            "challenges": challenges_count,
            "quiz_questions": quizzes_count
        }), 200
    finally:
        db.close()

@admin_bp.route("/worlds", methods=["POST"])
@admin_required
def create_world():
    data = request.get_json() or {}
    db = SessionLocal()
    try:
        w = World(
            number=data.get("number"),
            title=data.get("title"),
            goal=data.get("goal"),
            description=data.get("description"),
            final_project_title=data.get("final_project_title"),
            final_project_desc=data.get("final_project_desc")
        )
        db.add(w)
        db.commit()
        db.refresh(w)
        return jsonify({"world": w.to_dict()}), 201
    finally:
        db.close()
