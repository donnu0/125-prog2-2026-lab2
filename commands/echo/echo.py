import sys

def run(argv, ctx):
    # Вирізаємо назву команди
    args = argv[1:]

    # Якщо нічого не ввели, просто новий рядок
    if not args:
        print()
        return 0

    # Виводимо результат
    print(" ".join(args))
    return 0

# Тестування (виконується тільки при запуску цього файлу)
if __name__ == "__main__":
    run(["echo", "Тест", "системи"], None)


    


