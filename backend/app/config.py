import os
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def _load_secret_key() -> str:
    """Return a stable, private SECRET_KEY.

    Previously the app shipped a hard-coded secret, which means anybody with the
    source could forge login tokens.  Prefer the environment variable, otherwise
    generate a random key once and keep it in the (git-ignored) data directory.
    """
    env_key = os.environ.get("SECRET_KEY")
    if env_key:
        return env_key

    key_file = DATA_DIR / ".secret_key"
    try:
        if key_file.exists():
            stored = key_file.read_text(encoding="utf-8").strip()
            if stored:
                return stored
    except OSError:
        pass

    key = secrets.token_urlsafe(48)
    try:
        key_file.write_text(key, encoding="utf-8")
        # Best effort on POSIX; on Windows the file inherits the user's ACL.
        os.chmod(key_file, 0o600)
    except OSError:
        pass
    return key


class Config:
    SECRET_KEY = _load_secret_key()
    DATABASE_PATH = os.environ.get("DATABASE_PATH", str(DATA_DIR / "python_quest.db"))
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{DATABASE_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Code execution limits
    CODE_EXECUTION_TIMEOUT = int(os.environ.get("CODE_EXECUTION_TIMEOUT", "4"))  # seconds
    MAX_OUTPUT_LENGTH = int(os.environ.get("MAX_OUTPUT_LENGTH", "10000"))  # chars
    MAX_CODE_LENGTH = int(os.environ.get("MAX_CODE_LENGTH", "20000"))  # chars
    MAX_INPUT_LENGTH = int(os.environ.get("MAX_INPUT_LENGTH", "10000"))  # chars

    # Auth
    TOKEN_EXPIRY_DAYS = 30

    # CORS (comma separated).  "auto" allows localhost + private LAN origins,
    # which is what both the browser dev server and the Android WebView need.
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "auto")
