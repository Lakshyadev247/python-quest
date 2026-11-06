"""Sandbox bootstrap for learner-submitted Python code.

This file is executed in a *separate* interpreter (``python -I -X utf8
sandbox_runner.py solution.py``).  It adds two layers of protection on top of
the static AST checks:

1. A restricted ``__builtins__`` mapping (no open/eval/exec/compile/getattr/...).
2. A ``sys.addaudithook`` hook that denies process creation, network access,
   filesystem writes and imports outside the small educational allow-list.

The learning app is not a hardened multi-tenant execution service, but this
closes the trivial ``import os; os.popen(...)`` remote-code-execution hole and
makes accidental damage from learner code very unlikely.
"""

import builtins
import io
import os
import sys
import traceback
from types import SimpleNamespace

# Modules learners are allowed to use.  Everything else is rejected by both the
# guarded __import__ and the audit hook.  Keep this list to pure/educational
# libraries that do not expose OS or network primitives.
ALLOWED_IMPORTS = {
    "abc",
    "array",
    "base64",
    "binascii",
    "bisect",
    "calendar",
    "collections",
    "copy",
    "csv",
    "dataclasses",
    "datetime",
    "decimal",
    "enum",
    "fractions",
    "functools",
    "hashlib",
    "heapq",
    "io",
    "itertools",
    "json",
    "math",
    "numbers",
    "os",
    "operator",
    "random",
    "re",
    "sqlite3",
    "statistics",
    "string",
    "struct",
    "sys",
    "textwrap",
    "time",
    "typing",
    "unicodedata",
    "unittest",
    "_strptime",
}

# Learner programs may use only the harmless pieces required by the World 8-9
# exercises: path string helpers, an existence check scoped to the temporary
# exercise directory, and Python's major/minor version. They never receive the
# real os/sys modules or their process, environment, or filesystem controls.
def _safe_path_exists(path):
    try:
        root = os.path.realpath(os.getcwd())
        candidate = os.path.realpath(os.path.join(root, os.fspath(path)))
        if os.path.commonpath((root, candidate)) != root:
            return False
        return os.path.exists(candidate)
    except (TypeError, ValueError, OSError):
        return False

_SAFE_OS_PATH = SimpleNamespace(
    join=os.path.join,
    basename=os.path.basename,
    dirname=os.path.dirname,
    exists=_safe_path_exists,
)
_SAFE_OS = SimpleNamespace(path=_SAFE_OS_PATH)
_SAFE_SYS = SimpleNamespace(version_info=sys.version_info)

# Preload everything above *before* the audit hook is installed.  Several of
# these modules import os/sys internally; preloading avoids those imports
# tripping the hook later while keeping the allow-list strict.
_PRELOAD = sorted(ALLOWED_IMPORTS)
_PRIVATE_PRELOAD = ("traceback", "gc", "weakref")

# Files the traceback/linecache machinery may read (the learner's own script).
_READABLE_PATHS = set()

BLOCKED_EVENTS = {
    # process / privilege control
    "os.system",
    "os.exec",
    "os.spawn",
    "os.posix_spawn",
    "os.fork",
    "os.forkpty",
    "os.kill",
    "os.killpg",
    "os.setuid",
    "os.setgid",
    "os.setpgrp",
    "os.putenv",
    "os.unsetenv",
    "subprocess.Popen",
    "pty.spawn",
    # filesystem mutation / enumeration
    "os.remove",
    "os.unlink",
    "os.rmdir",
    "os.mkdir",
    "os.rename",
    "os.replace",
    "os.chmod",
    "os.chown",
    "os.link",
    "os.symlink",
    "os.truncate",
    "os.utime",
    "os.chdir",
    "os.listdir",
    "os.scandir",
    # network
    "socket.__new__",
    "socket.bind",
    "socket.connect",
    "socket.getaddrinfo",
    "socket.gethostbyname",
    "socket.gethostbyaddr",
    "socket.sendto",
    # native code / serialization escapes
    "ctypes.dlopen",
    "ctypes.dlsym",
    "ctypes.dlsym/handle",
    "ctypes.call_function",
    "ctypes.set_exception",
    "ctypes.get_errno",
    "ctypes.set_errno",
    "ctypes.get_last_error",
    "ctypes.set_last_error",
    "marshal.loads",
    "marshal.load",
    "pickle.find_class",
    # registry
    "winreg.OpenKey",
    "winreg.CreateKey",
    "winreg.SetValue",
    "winreg.DeleteKey",
    # debugger hooks
    "sys.settrace",
    "sys.setprofile",
    "sys.addaudithook",
    "sys.set_asyncgen_hooks",
    "resource.setrlimit",
    "resource.prlimit",
}

# Attribute names that are only useful for sandbox escapes.  ``__init__`` and
# the other normal dunder methods are intentionally allowed because the
# object-oriented lessons teach them.
BLOCKED_ATTRIBUTES = {
    "__bases__",
    "__base__",
    "__class__",
    "__closure__",
    "__code__",
    "__context__",
    "__dict__",
    "__func__",
    "__getattribute__",
    "__globals__",
    "__import__",
    "__loader__",
    "__mro__",
    "__reduce__",
    "__reduce_ex__",
    "__self__",
    "__spec__",
    "__subclasses__",
    "__traceback__",
    "ag_code",
    "ag_frame",
    "co_code",
    "co_consts",
    "co_names",
    "cr_code",
    "cr_frame",
    "f_back",
    "f_builtins",
    "f_code",
    "f_globals",
    "f_locals",
    "gi_code",
    "gi_frame",
    "tb_frame",
    "tb_next",
}

# Builtins removed from learner code.  ``__import__`` is replaced below with a
# guarded version so normal ``import math`` still works.
REMOVED_BUILTINS = {
    "open",
    "eval",
    "exec",
    "compile",
    "breakpoint",
    "globals",
    "locals",
    "vars",
    "getattr",
    "setattr",
    "delattr",
    "help",
    "exit",
    "quit",
    "copyright",
    "credits",
    "license",
    "memoryview",
}


def _real(path):
    try:
        return os.path.realpath(os.fspath(path))
    except (TypeError, ValueError, OSError):
        return ""


def _under(path, directory):
    path = os.path.normcase(_real(path))
    directory = os.path.normcase(_real(directory))
    if not path or not directory:
        return False
    return path == directory or path.startswith(directory + os.sep)


def _is_allowed_read(path, mode, flags):
    if isinstance(path, int):
        return False
    if mode and any(ch in str(mode) for ch in "wax+"):
        return False
    write_flags = 0
    for flag_name in ("O_WRONLY", "O_RDWR", "O_CREAT", "O_TRUNC", "O_APPEND"):
        write_flags |= getattr(os, flag_name, 0)
    if isinstance(flags, int) and flags & write_flags:
        return False
    # Import machinery may read the standard library; tracebacks may read the
    # learner's own script.  Nothing else on disk is readable.
    if any(_under(path, readable) for readable in _READABLE_PATHS):
        return True
    return _under(path, sys.base_prefix) or _under(path, sys.prefix)


def _audit(event, args):
    if event in ("sqlite3.connect", "sqlite3.connect/handle"):
        if event == "sqlite3.connect":
            target = str(args[0]) if args else ""
            if target not in (":memory:", ""):
                # Only allow local db files within the isolated sandbox temp directory (no traversal / drive letters)
                if ".." in target or "/" in target or "\\" in target or ":" in target:
                    raise PermissionError("Security restriction: SQLite database path must be a local file or ':memory:' in the learning sandbox.")
        return

    if event in BLOCKED_EVENTS:
        if event in ("os.listdir", "os.scandir"):
            # Importlib may enumerate directories inside the stdlib.  Allow that,
            # but not enumeration of the user's home directory.
            path = args[0] if args else None
            if path and (_under(path, sys.base_prefix) or _under(path, sys.prefix)):
                return
        raise PermissionError(
            f"Security restriction: '{event}' is disabled in the learning sandbox."
        )

    if event == "import":
        module_name = str(args[0]).split(".")[0]
        if module_name not in ALLOWED_IMPORTS:
            raise PermissionError(
                f"Security restriction: module '{module_name}' is disabled in the learning environment."
            )
        return

    if event == "open":
        path, mode, flags = (list(args) + [None, None, None])[:3]
        if not _is_allowed_read(path, mode, flags):
            raise PermissionError(
                "Security restriction: file access is disabled in the learning environment."
            )


def _guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
    root = str(name).split(".")[0]
    if level != 0 or root not in ALLOWED_IMPORTS:
        raise ImportError(
            f"Security restriction: module '{root}' is disabled in the learning environment."
        )
    if root == "os":
        return _SAFE_OS
    if root == "sys":
        return _SAFE_SYS
    return builtins.__import__(name, globals, locals, fromlist, level)


class _LimitedWriter(io.TextIOBase):
    """Cap captured output so a ``while True: print(...)`` cannot exhaust RAM."""

    def __init__(self, stream, limit):
        self._stream = stream
        self._limit = limit
        self._written = 0

    def write(self, text):
        if not isinstance(text, str):
            text = str(text)
        if self._written < self._limit:
            remaining = self._limit - self._written
            self._stream.write(text[:remaining])
        self._written += len(text)
        return len(text)

    def flush(self):
        try:
            self._stream.flush()
        except Exception:
            pass

    def isatty(self):
        return False


def main():
    if len(sys.argv) != 2:
        print("sandbox_runner: missing solution path", file=sys.stderr)
        return 2

    solution_path = sys.argv[1]
    try:
        _READABLE_PATHS.add(os.path.abspath(solution_path))
    except OSError:
        pass
    try:
        with open(solution_path, "r", encoding="utf-8", errors="replace") as fh:
            source = fh.read()
    except OSError as exc:
        print(f"sandbox_runner: cannot read solution: {exc}", file=sys.stderr)
        return 2

    # Keep the compiler outside the audit hook (the hook denies compile/eval
    # access to learner code, not to this bootstrap).
    try:
        code = compile(source, "solution.py", "exec")
    except SyntaxError as exc:
        print(f"SyntaxError: {exc}\n", file=sys.stderr)
        return 1

    try:
        for module_name in _PRELOAD + list(_PRIVATE_PRELOAD):
            try:
                builtins.__import__(module_name)
            except Exception:
                pass

        limit = int(os.environ.get("PYQUEST_OUTPUT_LIMIT", "10000"))
        sys.stdout = _LimitedWriter(sys.stdout, limit)
        sys.stderr = _LimitedWriter(sys.stderr, limit)

        safe_builtins = dict(vars(builtins))
        for name in REMOVED_BUILTINS:
            safe_builtins.pop(name, None)
        safe_builtins["__import__"] = _guarded_import

        sys.addaudithook(_audit)

        scope = {
            "__name__": "__main__",
            "__file__": "solution.py",
            "__builtins__": safe_builtins,
        }
        exec(code, scope, scope)
        return 0
    except SystemExit as exc:
        return int(exc.code) if isinstance(exc.code, int) else 0
    except BaseException:
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    raise SystemExit(main())
