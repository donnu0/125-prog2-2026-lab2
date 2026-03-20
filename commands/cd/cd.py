import os
import sys

def run(argv: list[str], ctx) -> int:
    """
    Змінює поточну робочу директорію командної оболонки.
    argv[0] - ім'я команди ('cd')
    argv[1:] - аргументи (шлях до директорії)
    Повертає цілий код завершення: 0 (успіх), 1 (помилка виконання), 2 (помилка аргументів).
    """
    # 1. Перевірка аргументів (Zero Trust)
    if len(argv) > 2:
        # Некоректний виклик: забагато аргументів
        sys.stderr.write("usage: cd [directory]\n") # usage-повідомлення у stderr
        return 2 # код завершення 2
    # Визначення цільової директорії
    if len(argv) == 1:
        # Якщо аргументів немає, переходимо в домашню директорію
        # Припускаємо, що ctx має словник env зі змінними середовища
        target_dir = ctx.env.get("HOME", "") if hasattr(ctx, 'env') else os.environ.get("HOME", "")
        if not target_dir:
            sys.stderr.write("cd: HOME variable not set\n")
            return 1 # Помилка виконання
    else:
        target_dir = argv[1]
    # 2. Виконання команди та обробка помилок (Zero Trust)
    try:
        # Спроба змінити директорію
        os.chdir(target_dir)
        # Оновлення контексту shell (якщо архітектура вашого minish цього вимагає)
        # У методичці вказано, що контекст містить поточний робочий каталог
        # Якщо ctx дозволяє зміну, це може виглядати так:
        if hasattr(ctx, 'cwd'):
            ctx.cwd = os.getcwd()
        return 0 # Успішне виконання
    except FileNotFoundError:
        sys.stderr.write(f"cd: {target_dir}: No such file or directory\n")
        return 1 # Помилка виконання (файл не знайдено)
    except PermissionError:
        sys.stderr.write(f"cd: {target_dir}: Permission denied\n")
        return 1 # Помилка виконання (доступ заборонено)
    except NotADirectoryError:
        sys.stderr.write(f"cd: {target_dir}: Not a directory\n")
        return 1 # Помилка виконання
    except Exception as e:
        # Глобальне перехоплення, щоб модуль ніколи не "падав" разом із shell
        # Коротке повідомлення в stderr, ніяких stack trace
        sys.stderr.write(f"cd: internal error\n")
        return 1 # При внутрішній помилці повертаємо 1
