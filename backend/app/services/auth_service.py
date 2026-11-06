import time
from functools import wraps
from flask import request, jsonify, g
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from app.config import Config
from app.models.user import User
from app.database import SessionLocal

serializer = URLSafeTimedSerializer(Config.SECRET_KEY)

def generate_token(user_id: int) -> str:
    return serializer.dumps({"user_id": user_id, "iat": int(time.time())})

def verify_token(token: str) -> int | None:
    try:
        data = serializer.loads(token, max_age=Config.TOKEN_EXPIRY_DAYS * 86400)
        return data.get("user_id")
    except (SignatureExpired, BadTimeSignature, Exception):
        return None

def get_current_user_id_from_request() -> int | None:
    auth_header = request.headers.get("Authorization")
    token = None
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
    elif request.cookies.get("token"):
        token = request.cookies.get("token")
    
    if not token:
        return None
        
    return verify_token(token)

def optional_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = get_current_user_id_from_request()
        g.user_id = user_id
        g.is_admin = False
        if user_id:
            db = SessionLocal()
            try:
                user = db.query(User).filter(User.id == user_id).first()
                if user:
                    g.is_admin = user.is_admin
            finally:
                db.close()
        return f(*args, **kwargs)
    return decorated

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = get_current_user_id_from_request()
        if not user_id:
            return jsonify({"error": "Authentication required", "status": "unauthorized"}), 401
        
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({"error": "User not found", "status": "unauthorized"}), 401
            g.user_id = user_id
            g.is_admin = user.is_admin
        finally:
            db.close()
            
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = get_current_user_id_from_request()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401
            
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user or not user.is_admin:
                return jsonify({"error": "Administrator privilege required"}), 403
            g.user_id = user_id
            g.is_admin = True
        finally:
            db.close()
            
        return f(*args, **kwargs)
    return decorated
