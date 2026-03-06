import shlex
import sys

def parse(command_line: str) -> list[str]:
    """
    Розбиває рядок вводу на список аргументів
    Ігнорує коментарі (символ #) та обробляє незакриті лапки.
'    """
    if not command_line or not command_line.strip():
        return []
    
    if len(command_line) > 4096:
        print("minish: parser error: command too long", file=sys.stderr)
        return []

    try:
        # comments=True дозволяє ігнорувати текст після #
        tokens = shlex.split(command_line, comments=True)
        return tokens
        
    except ValueError as e:
        print(f"minish: parser error: {e}", file=sys.stderr)
        return []


if __name__ == "__main__":
    print("--- Тестування парсера (введіть 'exit' для виходу) ---")
    while True:
        try:
            user_input = input("test> ")
            if user_input.strip() == "exit":
                break
            result = parse(user_input)
            print(f"Результат: {result}\n")
        except KeyboardInterrupt:
            print("\nВихід...")
            break