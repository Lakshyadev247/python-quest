import os
import re

from flask import Flask, jsonify
from flask_cors import CORS

from app.config import Config
from app.database import init_db
from app.routes import (
    auth_bp,
    curriculum_bp,
    progress_bp,
    quiz_bp,
    code_bp,
    gamification_bp,
    admin_bp,
)


def _cors_origins():
    """Return explicit origins or regexes for localhost + private LAN.

    The Android WebView uses ``https://localhost`` / ``capacitor://localhost``;
    the Vite dev server uses localhost or a private LAN address.  A public
    website is not allowed to call the API from a browser.
    """
    raw = (Config.CORS_ORIGINS or "auto").strip()
    if raw and raw != "auto":
        return [origin.strip() for origin in raw.split(",") if origin.strip()]

    patterns = [
        r"https?://localhost(:\d+)?",
        r"https?://127\.0\.0\.1(:\d+)?",
        r"https?://192\.168\.\d{1,3}\.\d{1,3}(:\d+)?",
        r"https?://10\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d+)?",
        r"https?://172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}(:\d+)?",
    ]
    origins = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    origins.append("capacitor://localhost")
    return origins


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Bearer-token auth means we do not need credentialed CORS.  Restricting
    # origins avoids exposing the API to arbitrary websites.
    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=False,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    )

    # Initialize Database tables
    init_db()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(curriculum_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(code_bp)
    app.register_blueprint(gamification_bp)
    app.register_blueprint(admin_bp)

    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "healthy",
            "service": "Python Quest API",
            "version": "1.0.0"
        }), 200

    return app
