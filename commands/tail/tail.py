import sys
from collections import deque

def run(argv: list[str], ctx) -> int:

    try:
        if len(argv) < 2:
            print("usage: tail [-n num] <file>", file=sys.stderr)
            return 2 

        n = 10
        filename = ""

        if argv[1] == '-n':
            if len(argv) < 4:
                print("tail: missing filename or number of lines", file=sys.stderr)
                print("usage: tail [-n num] <file>", file=sys.stderr)
                return 2
            
            try:
                n = int(argv[2])
                if n < 0:
                    raise ValueError
            except ValueError:
                print(f"tail: invalid number of lines: '{argv[2]}'", file=sys.stderr)
                return 2
            
            filename = argv[3]
        else:
            filename = argv[1]

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                last_lines = deque(f, maxlen=n)
                
                for line in last_lines:
                    sys.stdout.write(line)
                    
        except FileNotFoundError:
            print(f"tail: cannot open '{filename}' for reading: No such file or directory", file=sys.stderr)
            return 1 
        except PermissionError:
            print(f"tail: cannot open '{filename}' for reading: Permission denied", file=sys.stderr)
            return 1
        except OSError as e:
            print(f"tail: error reading file '{filename}': {e}", file=sys.stderr)
            return 1


        return 0

    except Exception as e:
        print(f"tail: internal error: {e}", file=sys.stderr)
        return 1
        _