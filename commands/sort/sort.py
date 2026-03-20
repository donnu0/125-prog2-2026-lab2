import sys

def run(argv: list[str], ctx) -> int:
    """
    Команда sort.
    argv[0] - слово 'sort'
    argv[1] - шлях до файлу
    """
    
    # Перевіряємо, чи користувач ввів назву файлу
    if len(argv) != 2:
        sys.stderr.write("Usage: sort <filename>\n")
        return 2

    filename = argv[1]

    # Пробуємо відкрити і відсортувати файл
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        lines.sort()

        # Виводимо відсортовані рядки
        for line in lines:
            sys.stdout.write(line)
            
        return 0

    except FileNotFoundError:
        sys.stderr.write(f"sort: {filename}: No such file or directory\n")
        return 1
        
    except PermissionError:
        sys.stderr.write(f"sort: {filename}: Permission denied\n")
        return 1
        
    except Exception:
        sys.stderr.write("sort: internal error occurred\n")
        return 1