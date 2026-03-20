import sys

def run(argv, ctx):
    print("RUNNING")

    args = argv[1:]

    if not args:
        print()
        return 0

    print(" ".join(args))
    return 0


if __name__ == "__main__":
    print("START")
    run(["echo", "Hello", "World"], None)
    


