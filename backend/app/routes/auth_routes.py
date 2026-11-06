from flask import Blueprint, request, jsonify, g
from app.database import SessionLocal
from app.models.user import User
from app.services.auth_service import generate_token, auth_required

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not username or len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters long"}), 400
    if not email or "@" not in email:
        return jsonify({"error": "Please provide a valid email address"}), 400
    if not password or len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400

    db = SessionLocal()
    try:
        if db.query(User).filter(User.username == username).first():
            return jsonify({"error": "Username is already taken"}), 409
        if db.query(User).filter(User.email == email).first():
            return jsonify({"error": "Email is already registered"}), 409

        user = User(
            username=username,
            email=email,
            is_admin=False
        )
        user.set_password(password)
        db.add(user)
        db.commit()
        db.refresh(user)

        token = generate_token(user.id)
        return jsonify({
            "message": "Account created successfully",
            "token": token,
            "user": user.to_dict()
        }), 201
    finally:
        db.close()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    identifier = data.get("username", "").strip()
    password = data.get("password", "")

    if not identifier or not password:
        return jsonify({"error": "Please provide username/email and password"}), 400

    db = SessionLocal()
    try:
        user = db.query(User).filter(
            (User.username == identifier) | (User.email == identifier.lower())
        ).first()

        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials"}), 401

        token = generate_token(user.id)
        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": user.to_dict()
        }), 200
    finally:
        db.close()

@auth_bp.route("/me", methods=["GET"])
@auth_required
def get_me():
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"user": user.to_dict()}), 200
    finally:
        db.close()

@auth_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logged out successfully"}), 200

@auth_bp.route("/profile", methods=["PUT"])
@auth_required
def update_profile():
    data = request.get_json() or {}
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == g.user_id).first()
        if not user:
            return jsonify({"error": "User not found"}), 404
        if "avatar" in data:
            user.avatar = str(data["avatar"])[:100]
        if "theme" in data and data["theme"] in ("dark", "light"):
            user.theme = data["theme"]
        db.commit()
        db.refresh(user)
        return jsonify({"user": user.to_dict()}), 200
    finally:
        db.close()
