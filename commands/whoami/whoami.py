import getpass
import sys


def run(argv, ctx):
    try:
        # whoami не приймає аргументи
        if len(argv) > 1:
            print("usage: whoami", file=sys.stderr)
            return 2

        print(getpass.getuser())
        return 0

    except Exception:
        print("whoami: execution error", file=sys.stderr)
        return 1
