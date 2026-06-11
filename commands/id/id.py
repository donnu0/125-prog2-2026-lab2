import getpass
import os
import sys


USAGE = "usage: id"


def _read_numeric_id(function_name: str):
    reader = getattr(os, function_name, None)
    if not callable(reader):
        return "N/A"

    try:
        return reader()
    except Exception:
        return "N/A"


def run(argv: list[str], ctx) -> int:
    if not isinstance(argv, (list, tuple)) or len(argv) != 1 or argv[0] != "id":
        print(USAGE, file=sys.stderr)
        return 2

    try:
        user = getpass.getuser()
        uid = _read_numeric_id("getuid")
        gid = _read_numeric_id("getgid")
        print(f"uid={uid} gid={gid} user={user}")
        return 0
    except Exception:
        print("id: internal error", file=sys.stderr)
        return 1
