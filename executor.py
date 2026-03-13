import commands.supported

def execute(args: list[str]):
    if args[0] in commands.supported.COMMANDS:
        commands.supported.COMMANDS[args[0]].run(args, [])
    else:
        print(f"Command '{args[0]}' not found")