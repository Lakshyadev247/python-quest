from flask import Blueprint, jsonify, request, g
from app.database import SessionLocal
from app.models.curriculum import World, Level, Lesson
from app.models.progress import UserProgress
from app.models.user import User
from app.services.auth_service import get_current_user_id_from_request
from app.services.progress_service import is_level_unlocked

curriculum_bp = Blueprint("curriculum", __name__, url_prefix="/api")

@curriculum_bp.route("/worlds", methods=["GET"])
def get_worlds():
    user_id = get_current_user_id_from_request()
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first() if user_id else None
        worlds = db.query(World).order_by(World.number).all()
        result = []

        completed_level_ids = set()
        if user:
            completed_records = db.query(UserProgress.level_id).filter(
                UserProgress.user_id == user.id,
                UserProgress.is_level_completed == True
            ).all()
            completed_level_ids = {r[0] for r in completed_records}

        for idx, w in enumerate(worlds):
            w_dict = w.to_dict()
            total_levels = len(w.levels)
            completed_in_world = sum(1 for lvl in w.levels if lvl.id in completed_level_ids)
            
            if idx == 0 or (user and user.is_admin):
                unlocked = True
            else:
                prev_world = worlds[idx - 1]
                prev_levels = [lvl.id for lvl in prev_world.levels]
                unlocked = all(pid in completed_level_ids for pid in prev_levels) if prev_levels else True

            w_dict["completed_levels"] = completed_in_world
            w_dict["is_unlocked"] = unlocked
            w_dict["completion_percent"] = round((completed_in_world / total_levels * 100), 1) if total_levels > 0 else 0
            result.append(w_dict)

        return jsonify({"worlds": result}), 200
    finally:
        db.close()

@curriculum_bp.route("/worlds/<int:world_id>", methods=["GET"])
def get_world(world_id):
    user_id = get_current_user_id_from_request()
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first() if user_id else None
        world = db.query(World).filter(World.id == world_id).first()
        if not world:
            return jsonify({"error": "World not found"}), 404

        levels_data = []
        for lvl in world.levels:
            lvl_dict = lvl.to_dict()
            if user:
                prog = db.query(UserProgress).filter(
                    UserProgress.user_id == user.id,
                    UserProgress.level_id == lvl.id
                ).first()
                unlocked = is_level_unlocked(db, user.id, lvl.id) or user.is_admin
                lvl_dict["is_unlocked"] = unlocked
                lvl_dict["user_progress"] = prog.to_dict() if prog else None
            else:
                lvl_dict["is_unlocked"] = (world.number == 1 and lvl.order_index == 1)
                lvl_dict["user_progress"] = None
            levels_data.append(lvl_dict)

        w_dict = world.to_dict()
        w_dict["levels"] = levels_data
        return jsonify({"world": w_dict}), 200
    finally:
        db.close()

@curriculum_bp.route("/levels/<int:level_id>", methods=["GET"])
def get_level(level_id):
    user_id = get_current_user_id_from_request()
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first() if user_id else None
        level = db.query(Level).filter(Level.id == level_id).first()
        if not level:
            return jsonify({"error": "Level not found"}), 404

        unlocked = False
        if user and user.is_admin:
            unlocked = True
        elif user:
            unlocked = is_level_unlocked(db, user.id, level_id)
        else:
            unlocked = (level.world.number == 1 and level.order_index == 1)

        level_dict = level.to_dict(include_details=True)
        level_dict["is_unlocked"] = unlocked

        if user:
            prog = db.query(UserProgress).filter(
                UserProgress.user_id == user.id,
                UserProgress.level_id == level_id
            ).first()
            level_dict["user_progress"] = prog.to_dict() if prog else None
        else:
            level_dict["user_progress"] = None

        return jsonify({"level": level_dict}), 200
    finally:
        db.close()

@curriculum_bp.route("/lessons/<int:level_id>", methods=["GET"])
def get_lesson(level_id):
    db = SessionLocal()
    try:
        lesson = db.query(Lesson).filter(Lesson.level_id == level_id).first()
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404
        return jsonify({"lesson": lesson.to_dict()}), 200
    finally:
        db.close()
