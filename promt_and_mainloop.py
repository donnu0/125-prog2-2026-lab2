import os
import platform

login=os.getlogin()

host_name=platform.node()

catalog=os.getcwd()

total=login+"@"+host_name+":"+catalog+"$"

while True:
    
    # 1. Prompt та прийом команди
    user_input = input(total)
    
    # Перевірка на порожній ввід
    if not user_input:
        continue
    
    print("Команда для виконання:", user_input)