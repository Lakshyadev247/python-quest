"""Small in-memory rate limiter for expensive endpoints.

The backend is a single-process development server, so a process-local bucket
is sufficient.  If it is ever deployed with multiple workers, move this to
Redis or similar.
"""

import time
from collections import defaultdict, deque
from functools import wraps

from flask import g, jsonify, request

_buckets = defaultdict(deque)


def rate_limit(limit: int = 30, window: int = 60):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            identity = str(getattr(g, "user_id", "anonymous"))
            key = f"{identity}:{request.remote_addr or 'unknown'}"
            now = time.monotonic()
            bucket = _buckets[key]

            while bucket and bucket[0] <= now - window:
                bucket.popleft()

            if len(bucket) >= limit:
                retry_after = max(0.0, window - (now - bucket[0]))
                response = jsonify({
                    "error": "Too many requests. Please wait a moment and try again.",
                    "retry_after": round(retry_after, 1),
                })
                response.status_code = 429
                response.headers["Retry-After"] = str(int(retry_after) + 1)
                return response

            bucket.append(now)

            # Opportunistic cleanup so the dictionary cannot grow forever.
            if len(_buckets) > 2048:
                for old_key in list(_buckets):
                    if not _buckets[old_key]:
                        del _buckets[old_key]

            return func(*args, **kwargs)

        return wrapper
    return decorator
