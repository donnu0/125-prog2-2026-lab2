import sys
import os


def run(argv: list[str], ctx) -> int:
    """
    argv[0] - "cat"
    argv[1:] - файли
    """

    # якщо немає аргументів → usage
    if len(argv) < 2:
        print("usage: cat <file1> [file2 ...]", file=sys.stderr)
        return 2

    exit_code = 0

    for path in argv[1:]:
        try:
            # перевірка існування
            if not os.path.exists(path):
                print(f"cat: {path}: No such file or directory", file=sys.stderr)
                exit_code = 1
                continue

            # перевірка, що це файл
            if os.path.isdir(path):
                print(f"cat: {path}: Is a directory", file=sys.stderr)
                exit_code = 1
                continue

            # відкриття і читання
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    try:
                        print(line, end="")
                    except Exception:
                        print("cat: write error", file=sys.stderr)
                        return 1

        except PermissionError:
            print(f"cat: {path}: Permission denied", file=sys.stderr)
            exit_code = 1

        except Exception:
            print(f"cat: {path}: Unknown error", file=sys.stderr)
            exit_code = 1

    return exit_code