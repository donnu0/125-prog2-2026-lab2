import sys

def run(argv: list[str], ctx) -> int:
    """
    argv[0] - ім’я команди (pwd)
    argv[1:] - аргументи
    ctx - об'єкт контексту shell, який містить поточний каталог
    """
    # Перевірка на Zero Trust: pwd не повинна приймати зайвих аргументів
    if len(argv) > 1:
        sys.stderr.write("Usage: pwd\n")
        sys.stderr.write("Error: pwd command does not accept arguments.\n")
        return 2  # Код 2 за контрактом — помилка використання/аргументів
    
    try:
        # Спроба отримати каталог з контексту shell (за контрактом 3.2.2)
        if hasattr(ctx, 'current_dir'):
            current_directory = ctx.current_dir
        elif hasattr(ctx, 'cwd'):
            current_directory = ctx.cwd
        else:
            import os
            current_directory = os.getcwd()
            
        # Нормальний вивід пишемо в stdout
        sys.stdout.write(f"{current_directory}\n")
        return 0  # Код 0 — успішне виконання
        
    except Exception as e:
        # Якщо щось пішло не так — виводимо помилку в stderr і не даємо shell впасти
        sys.stderr.write(f"pwd: internal error: {str(e)}\n")
        return 1  # Код 1 — помилка виконання
