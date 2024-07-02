import os
import json
import sys

width = os.get_terminal_size(0).columns

# Decorations
LINE = "-" * width

# System info for testing
USERNAME = "user"  # Get username from TripleOS

with open("command_list.json", "r", encoding="utf-8") as json_file:
    command_list = json.load(json_file)

def show_welcome_message():
    print(f"Welcome to PyLite".center(width))
    print("PyLite - минималистичное и простое окружение для TripleOS".center(width))
    print(LINE)

show_welcome_message()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

    show_welcome_message()

def show_help():
    for command in command_list:
        print(f"{command['name']} - {command['description']}")

while True:
    cmd = input(f"{USERNAME}> $ ")

    found = False
    for command in command_list:
        if command["name"] == cmd.lower().strip():
            exec(command["action"])
            found = True
            break

    if not found:
        print(f"Ошибка: {cmd} не является исполняемой программой.")
        print("Введите help для вывода списка команд")