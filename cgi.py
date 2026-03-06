"""
Minimal compatibility shim for the removed `cgi` stdlib module
This provides a simple `parse_header` and a lightweight `FieldStorage`
implementation sufficient for basic Django 3.1 usage (content-type parsing
and avoiding import errors). It's intended for local development only.
"""
from typing import Tuple, Dict

def parse_header(line: str) -> Tuple[str, Dict[str, str]]:
    """Parse a Content-Type like header into (value, params dict).

    Example: 'text/html; charset=utf-8' -> ('text/html', {'charset': 'utf-8'})
    """
    if not line:
        return '', {}
    parts = [p.strip() for p in line.split(';')]
    value = parts[0].lower()
    params = {}
    for p in parts[1:]:
        if '=' in p:
            k, v = p.split('=', 1)
            k = k.strip().lower()
            v = v.strip().strip('"')
            params[k] = v
    return value, params


class FieldStorage:
    """Very small stub of cgi.FieldStorage.

    This stub intentionally does not implement multipart parsing. It's only
    present to satisfy imports in environments where the stdlib `cgi` was
    removed (Python 3.13+). For file uploads or advanced form handling use a
    Python version compatible with Django 3.1.
    """
    def __init__(self, *args, **kwargs):
        self.filename = None
        self.value = None

    def __repr__(self):
        return '<FieldStorage (shim)>'


# Provide commonly referenced names to avoid AttributeError on import
escape = lambda s: s
