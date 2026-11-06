"""One-request JSON adapter used by the Vite live-preview middleware."""
import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parent
ROOT = BACKEND.parent
CURRICULUM = ROOT / "frontend" / "src" / "data" / "curriculum.json"
sys.path.insert(0, str(BACKEND))

from app.services.executor_service import execute_python_code


def submit_code(data):
    challenge_id = data.get("challenge_id")
    code = data.get("code", "")
    if not challenge_id or not isinstance(code, str) or not code:
        return {"error": "challenge_id and code are required"}, 400

    curriculum = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    challenge = next(
        (
            item
            for level in curriculum["levels"].values()
            for item in level.get("challenges", [])
            if str(item.get("id")) == str(challenge_id)
        ),
        None,
    )
    if challenge is None:
        try:
            cid = int(challenge_id)
            if 1 <= cid <= 126:
                mapped_id = cid + 1299
                challenge = next(
                    (
                        item
                        for level in curriculum["levels"].values()
                        for item in level.get("challenges", [])
                        if item.get("id") == mapped_id
                    ),
                    None,
                )
        except (ValueError, TypeError):
            pass

    if challenge is None:
        try:
            import sqlite3
            db_path = BACKEND / "data" / "python_quest.db"
            if db_path.exists():
                conn = sqlite3.connect(str(db_path))
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT * FROM coding_challenges WHERE id = ?", (challenge_id,))
                row = cur.fetchone()
                if row:
                    cur.execute("SELECT * FROM test_cases WHERE challenge_id = ?", (challenge_id,))
                    tcs = [dict(tc) for tc in cur.fetchall()]
                    challenge = dict(row)
                    challenge["test_cases"] = tcs
                conn.close()
        except Exception:
            pass

    if challenge is None:
        return {"error": "Challenge not found"}, 404

    results = []
    passed_count = 0
    stdout = stderr = ""
    cases = challenge.get("test_cases", [])
    for index, test in enumerate(cases, 1):
        run = execute_python_code(code, test.get("input_data", ""))
        actual = run["stdout"].rstrip()
        expected = test.get("expected_output", "").rstrip()
        passed = run["success"] and actual == expected
        passed_count += int(passed)
        stdout, stderr = run["stdout"], run["stderr"]
        hidden = bool(test.get("is_hidden", False))
        results.append({
            "test_index": index,
            "passed": passed,
            "input": "<hidden>" if hidden else test.get("input_data", ""),
            "expected_output": "<hidden>" if hidden else expected,
            "actual_output": actual if not hidden or passed else "<output mismatch>",
            "stderr": run["stderr"] if not passed else "",
            "is_hidden": hidden,
        })

    return {
        "passed": bool(cases) and passed_count == len(cases),
        "tests_passed": passed_count,
        "total_tests": len(cases),
        "test_results": results,
        "stdout": stdout,
        "stderr": stderr,
        "is_guest": True,
    }, 200


def main():
    try:
        request = json.load(sys.stdin)
        action = request.get("action")
        data = request.get("data") or {}
        if action == "execute":
            code = data.get("code", "")
            input_data = data.get("input", "")
            if not isinstance(code, str) or not code:
                response, status = {"error": "No Python code provided"}, 400
            elif not isinstance(input_data, str):
                response, status = {"error": "input must be text"}, 400
            else:
                response, status = execute_python_code(code, input_data), 200
        elif action == "submit":
            response, status = submit_code(data)
        else:
            response, status = {"error": "Unknown code action"}, 400
        sys.stdout.write(json.dumps({"status": status, "body": response}))
    except Exception as exc:  # Keep failures as JSON so the browser gets a useful error.
        sys.stdout.write(json.dumps({"status": 500, "body": {"error": str(exc)}}))


if __name__ == "__main__":
    main()
