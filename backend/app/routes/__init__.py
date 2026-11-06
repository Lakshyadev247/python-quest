from app.routes.auth_routes import auth_bp
from app.routes.curriculum_routes import curriculum_bp
from app.routes.progress_routes import progress_bp
from app.routes.quiz_routes import quiz_bp
from app.routes.code_routes import code_bp
from app.routes.gamification_routes import gamification_bp
from app.routes.admin_routes import admin_bp

__all__ = [
    "auth_bp",
    "curriculum_bp",
    "progress_bp",
    "quiz_bp",
    "code_bp",
    "gamification_bp",
    "admin_bp"
]
