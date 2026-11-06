import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if sys.stdout is None:
    sys.stdout = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "server.log"), "a", encoding="utf-8")
elif hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if sys.stderr is None:
    sys.stderr = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "server_err.log"), "a", encoding="utf-8")
elif hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from app import create_app
from app.database import SessionLocal
from app.seed_curriculum import seed_curriculum

app = create_app()

def initialize():
    db = SessionLocal()
    try:
        seed_curriculum(db)
    finally:
        db.close()

if __name__ == "__main__":
    initialize()
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    if sys.stdout is not None:
        print(f"[+] Python Quest Backend running at http://{host}:{port}")
        if host == "0.0.0.0":
            import socket
            try:
                lan_ip = socket.gethostbyname(socket.gethostname())
                print(f"[+] On your phone use: http://{lan_ip}:{port}/api")
            except OSError:
                pass
    app.run(host=host, port=port, debug=False, use_reloader=False)
