import os
import sys
import threading
import time
import socket
import webbrowser
from pathlib import Path

# If invoked as sandbox runner:
if len(sys.argv) >= 3 and sys.argv[1] == "__sandbox__":
    solution_file = sys.argv[2]
    sys.argv = [sys.argv[0], solution_file]
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    
    # Ensure backend directory is in sys.path
    if getattr(sys, "frozen", False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    if bundle_dir not in sys.path:
        sys.path.insert(0, bundle_dir)

    from app.services.sandbox_runner import main as sandbox_main
    raise SystemExit(sandbox_main())

# Normal desktop application startup:
from flask import send_from_directory

# 1. Determine paths
if getattr(sys, "frozen", False):
    BUNDLE_DIR = sys._MEIPASS
    FRONTEND_DIST = os.path.join(BUNDLE_DIR, "frontend_dist")
    APP_DIR = os.path.dirname(sys.executable)
    INITIAL_DB = os.path.join(BUNDLE_DIR, "data", "python_quest.db")
else:
    BASE_DIR = Path(__file__).resolve().parent.parent
    FRONTEND_DIST = str(BASE_DIR / "frontend" / "dist")
    APP_DIR = str(BASE_DIR)
    INITIAL_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "python_quest.db")

# 2. Database path (store in LocalAppData for permanence on user's machine)
USER_DATA_DIR = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "PythonQuest")
os.makedirs(USER_DATA_DIR, exist_ok=True)
USER_DB_PATH = os.path.join(USER_DATA_DIR, "python_quest.db")

if not os.path.exists(USER_DB_PATH) and os.path.exists(INITIAL_DB):
    import shutil
    try:
        shutil.copy2(INITIAL_DB, USER_DB_PATH)
    except Exception:
        pass

os.environ["DATABASE_PATH"] = USER_DB_PATH
os.environ["DATABASE_URL"] = f"sqlite:///{USER_DB_PATH}"

BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from app import create_app
from app.database import SessionLocal
from app.seed_curriculum import seed_curriculum

app = create_app()

# Initialize DB & Seed curriculum
try:
    db = SessionLocal()
    seed_curriculum(db)
    db.close()
except Exception as e:
    print(f"Curriculum init note: {e}")

# Register SPA routes to serve frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_spa(path):
    if path and os.path.exists(os.path.join(FRONTEND_DIST, path)):
        return send_from_directory(FRONTEND_DIST, path)
    return send_from_directory(FRONTEND_DIST, "index.html")

def find_free_port(preferred=5000):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", preferred))
        s.close()
        return preferred
    except OSError:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
        s.close()
        return port

def run_server(port):
    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)

def main():
    port = find_free_port(5000)
    server_thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()
    
    app_url = f"http://127.0.0.1:{port}"
    print(f"[+] Python Quest Desktop running at {app_url}")
    
    # Try opening with pywebview for a sleek native desktop window
    try:
        import webview
        window = webview.create_window(
            title="Python Quest",
            url=app_url,
            width=1280,
            height=820,
            min_size=(960, 600)
        )
        webview.start()
    except Exception as e:
        print(f"[!] pywebview fallback to default browser: {e}")
        webbrowser.open(app_url)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
