import os
import platform
import parser
import executor
import getpass

login=getpass.getuser()

host_name=platform.node()

while True:
# Динамічно отримуємо новий шлях на кожній ітерації циклу
    catalog=os.getcwd()
    total=login+"@"+host_name+":"+catalog+"$ "


# 1. Prompt та прийом команди
    user_input = input(total)

    # Перевірка на порожній ввід
    if not user_input:
        continue

    parse_result = parser.parse(user_input)
    executor.execute(parse_result)

