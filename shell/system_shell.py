import os
import json
import sys

with open("command_list.json", "r", encoding="utf-8") as json_file:
    command_list = json.load(json_file)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    for command in command_list:
        print(f"{command['name']} - {command['description']}")

while True:
    cmd = input("$ ")

    found = False
    for command in command_list:
        if command["name"] == cmd.lower().strip():
            exec(command["action"])
            found = True
            break

    if not found:
        print(f"Ошибка: {cmd} не является исполняемой программой.")
        print("Введите help для вывода списка команд")