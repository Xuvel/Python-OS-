import os
import json
import sys

with open("command_list.json", "r", encoding="utf-8") as json_file:
    command_list = json.load(json_file)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    for command in command_list:
        args = f"{command['args']} " if 'args' in command else ""
        print(f"{command['name']} {args}- {command['description']}")

def execute_command(cmd_name, args):
    for command in command_list:
        if command["name"] == cmd_name:
            try:
                exec(command["action"])
            except Exception as e:
                print(f"Ошибка при выполнении команды {cmd_name}: {e}")
            return True
    return False

while True:
    cmd = input("$ ")

    cmd_parts = cmd.lower().strip().split()
    try:
        cmd_name = cmd_parts[0]
        args = cmd_parts[1:]
    except IndexError:
        print("Команда не может быть пустой")
        continue

    if cmd_name == "exit":
        sys.exit(0)
    elif cmd_name == "clear":
        clear_terminal()
    elif cmd_name == "help":
        show_help()
    else:
        if not execute_command(cmd_name, args):
            print(f"Ошибка: {cmd_name} не является исполняемой программой.")
            print("Введите help для вывода списка команд")
