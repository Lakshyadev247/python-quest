import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile

from app.config import Config

RUNNER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sandbox_runner.py")
RUNTIME_TEMP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "runtime-tmp"))
os.makedirs(RUNTIME_TEMP_DIR, exist_ok=True)

# Modules that expose OS, network, process or introspection primitives.  The
# runtime sandbox also blocks these, but rejecting them up-front gives learners
# a clear, friendly error instead of a traceback.
BLOCKED_MODULES = {
    "asyncio", "builtins", "code", "codeop", "crypt", "ctypes", "fcntl",
    "fileinput", "ftplib", "gc", "getpass", "glob", "grp", "http", "httpx",
    "imaplib", "importlib", "inspect", "marshal", "mmap", "multiprocessing",
    "nt", "pathlib", "pdb", "pickle", "platform", "poplib", "posix",
    "pty", "pwd", "requests", "resource", "select", "selectors", "shutil",
    "signal", "smtplib", "socket", "socketserver", "ssl", "subprocess",
    "telnetlib", "tempfile", "termios", "threading", "tkinter", "trace",
    "turtle", "urllib", "webbrowser", "winreg", "xmlrpc",
    # private/implementation modules
    "_ctypes", "_io", "_marshal", "_os", "_pickle", "_socket", "_subprocess",
    "_winapi", "_winreg",
}

BLOCKED_CALLS = {
    "compile", "delattr", "eval", "exec", "exit", "fork", "getattr", "globals",
    "kill", "locals", "open", "popen", "quit", "setattr", "spawn", "system",
    "vars", "__import__",
}

BLOCKED_ATTRIBUTES = {
    "__bases__", "__base__", "__class__", "__closure__", "__code__", "__context__",
    "__dict__", "__func__", "__getattribute__", "__globals__", "__import__",
    "__loader__", "__mro__", "__reduce__", "__reduce_ex__", "__self__", "__spec__",
    "__subclasses__", "__traceback__", "ag_code", "ag_frame", "co_code", "co_consts",
    "co_names", "cr_code", "cr_frame", "f_back", "f_builtins", "f_code", "f_globals",
    "f_locals", "gi_code", "gi_frame", "tb_frame", "tb_next",
}


def analyze_code_safety(code: str) -> tuple[bool, str]:
    """Static AST analysis to reject obviously dangerous constructs."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        # Let the real interpreter produce the detailed syntax error.
        return True, ""
    except Exception as exc:
        return False, f"Invalid code syntax: {exc}"

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_pkg = alias.name.split(".")[0]
                if root_pkg in BLOCKED_MODULES:
                    return False, (
                        f"module '{root_pkg}' is disabled in the learning environment."
                    )
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                return False, "relative imports are disabled in the learning environment."
            if node.module:
                root_pkg = node.module.split(".")[0]
                if root_pkg in BLOCKED_MODULES:
                    return False, (
                        f"module '{root_pkg}' is disabled in the learning environment."
                    )
        elif isinstance(node, ast.Attribute):
            if node.attr in BLOCKED_ATTRIBUTES:
                return False, f"access to '{node.attr}' is restricted."
        elif isinstance(node, ast.Call):
            func = node.func
            name = func.id if isinstance(func, ast.Name) else (
                func.attr if isinstance(func, ast.Attribute) else None
            )
            if name in BLOCKED_CALLS:
                return False, f"function '{name}' is disabled in the learning environment."

    return True, ""


def sanitize_output(text: str) -> str:
    """Sanitize execution output and errors to ensure no host PC paths, usernames,
    storage details, or system hardware specs are ever revealed to the learner."""
    if not text:
        return ""
    cleaned = text

    # 1. Replace temporary script/runner paths in tracebacks with standard clean filename
    cleaned = re.sub(r'File ".*?[\\/](?:script|runner|sandbox_runner|test_runner)\.py"', 'File "solution.py"', cleaned)
    cleaned = re.sub(r'File ".*?[\\/]([a-zA-Z0-9_\-\.]+?\.py)"', r'File "\1"', cleaned)

    # 2. Strip user profile / home directory paths
    try:
        user_home = os.path.expanduser("~")
        if user_home and len(user_home) > 2:
            cleaned = cleaned.replace(user_home, "")
            cleaned = cleaned.replace(user_home.replace("\\", "/"), "")
    except Exception:
        pass

    # 3. Strip any Windows user paths like C:\Users\<username>\...
    cleaned = re.sub(r'[A-Za-z]:\\[Uu]sers\\[^\\]+[\\/]?', '', cleaned)
    cleaned = re.sub(r'/home/[^/]+[\\/]?', '', cleaned)
    cleaned = re.sub(r'/Users/[^/]+[\\/]?', '', cleaned)

    # 4. Strip AppData, Temp, Python installation paths
    cleaned = re.sub(r'[A-Za-z]:\\[Aa]pp[Dd]ata\\[^\\]+[\\/]?', '', cleaned)
    cleaned = re.sub(r'[A-Za-z]:\\[Pp]rogram\s*[Ff]iles(?:\s*\(x86\))?\\[^\\]+[\\/]?', '', cleaned)
    cleaned = re.sub(r'[A-Za-z]:\\[Pp]ython\d*\\[^\\]+[\\/]?', '', cleaned)

    # 5. Strip local drive prefixes like C:\ or D:\
    cleaned = re.sub(r'\b[A-Za-z]:\\', '', cleaned)

    return cleaned


def execute_python_code(code: str, input_data: str = "", timeout: int = None) -> dict:
    """Execute Python in a separate, restricted interpreter."""
    if timeout is None:
        timeout = Config.CODE_EXECUTION_TIMEOUT

    if len(code) > Config.MAX_CODE_LENGTH:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"InputError: code exceeds the {Config.MAX_CODE_LENGTH} character limit.\n",
            "timed_out": False,
            "exit_code": 1,
        }

    if len(input_data) > Config.MAX_INPUT_LENGTH:
        input_data = input_data[: Config.MAX_INPUT_LENGTH]

    is_safe, error_msg = analyze_code_safety(code)
    if not is_safe:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"SecurityError: Security restriction: {error_msg}\n",
            "timed_out": False,
            "exit_code": 1,
        }

    # Use the application's own writable runtime folder. Windows AppContainer
    # installs can deny writes to the system TEMP directory, which otherwise
    # makes even harmless learner code fail before it starts.
    temp_dir = tempfile.mkdtemp(prefix="pyquest_sandbox_", dir=RUNTIME_TEMP_DIR)
    script_path = os.path.join(temp_dir, "solution.py")

    try:
        with open(script_path, "w", encoding="utf-8") as fh:
            fh.write(code)

        clean_env = {
            "PYTHONIOENCODING": "utf-8",
            "PYTHONUTF8": "1",
            "PYQUEST_OUTPUT_LIMIT": str(Config.MAX_OUTPUT_LENGTH),
            "SYSTEMROOT": os.environ.get("SYSTEMROOT", "C:\\Windows"),
            "SYSTEMDRIVE": os.environ.get("SYSTEMDRIVE", "C:"),
            "TEMP": os.environ.get("TEMP", os.environ.get("TMP", "C:\\Windows\\Temp")),
            "TMP": os.environ.get("TMP", os.environ.get("TEMP", "C:\\Windows\\Temp")),
            "LOCALAPPDATA": os.environ.get("LOCALAPPDATA", ""),
            "USERPROFILE": os.environ.get("USERPROFILE", ""),
            "PATH": os.environ.get("PATH", ""),
        }
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            clean_env["_MEIPASS2"] = sys._MEIPASS

        # -I: isolated mode (ignore env vars and user site-packages)
        # -X utf8: consistent UTF-8 I/O on Windows
        if getattr(sys, "frozen", False):
            cmd = [sys.executable, "__sandbox__", script_path]
        else:
            cmd = [sys.executable, "-I", "-X", "utf8", RUNNER_PATH, script_path]

        proc = subprocess.run(
            cmd,
            input=input_data,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            cwd=temp_dir,
            env=clean_env,
            encoding="utf-8",
            errors="replace",
        )

        return {
            "success": proc.returncode == 0,
            "stdout": sanitize_output(proc.stdout[: Config.MAX_OUTPUT_LENGTH]),
            "stderr": sanitize_output(proc.stderr[: Config.MAX_OUTPUT_LENGTH]),
            "timed_out": False,
            "exit_code": proc.returncode,
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": (
                f"TimeoutError: Execution exceeded {timeout} seconds limit. "
                "Check for infinite loops or blocking operations.\n"
            ),
            "timed_out": True,
            "exit_code": -1,
        }
    except Exception as exc:
        return {
            "success": False,
            "stdout": "",
            "stderr": sanitize_output(f"ExecutionError: {exc}\n"),
            "timed_out": False,
            "exit_code": 1,
        }
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def run_test_cases(code: str, test_cases: list) -> dict:
    """Validate learner code against the challenge's test cases."""
    results = []
    passed_count = 0
    total_tests = len(test_cases)
    last_stdout = ""
    last_stderr = ""

    for idx, tc in enumerate(test_cases):
        input_data = getattr(tc, "input_data", "") or ""
        expected = getattr(tc, "expected_output", "") or ""
        is_hidden = getattr(tc, "is_hidden", False)

        run_res = execute_python_code(code, input_data=input_data)
        actual_output = run_res["stdout"].rstrip()
        expected_output = expected.rstrip()

        last_stdout = run_res["stdout"]
        last_stderr = run_res["stderr"]

        is_passed = run_res["success"] and actual_output == expected_output
        if is_passed:
            passed_count += 1

        results.append({
            "test_index": idx + 1,
            "passed": is_passed,
            "input": "<hidden>" if is_hidden else input_data,
            "expected_output": "<hidden>" if is_hidden else expected_output,
            "actual_output": actual_output if not is_hidden or is_passed else "<output mismatch>",
            "stderr": run_res["stderr"] if not is_passed else "",
            "is_hidden": is_hidden,
        })

    all_passed = total_tests > 0 and passed_count == total_tests

    return {
        "all_passed": all_passed,
        "tests_passed": passed_count,
        "total_tests": total_tests,
        "test_results": results,
        "stdout": last_stdout,
        "stderr": last_stderr,
    }
