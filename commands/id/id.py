import getpass
import os
import sys


USAGE = "usage: id"


def run(argv: list[str], ctx) -> int:
    if not isinstance(argv, (list, tuple)) or len(argv) != 1 or argv[0] != "id":
        print(USAGE, file=sys.stderr)
        return 2

    try:
        uid = os.getuid() if hasattr(os, "getuid") else "N/A"
        gid = os.getgid() if hasattr(os, "getgid") else "N/A"
        print(f"uid={uid} gid={gid} user={getpass.getuser()}")
        return 0
    except Exception:
        print("id: internal error", file=sys.stderr)
        return 1
