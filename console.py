import os
import time
import subprocess

import apps.calculator
import System

def mainDir():
	return os.getcwd()

if (os.name == "nt"):
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')

command_list = ["help", "stop"]
version = "v.0.1"
is_running = True
user_input = ""
error_level = 0x0
cum_times = 0

history = []

def s(command): # блять повесся нахуй с СВОими ебанными НАЗВАНИЯМИ БЛЯТЬ ИДИ НАХУЙ ЧМОШН ИК ЕБАННЫЙ АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААВРДЖПОЬЬЬЬЬЬЬЬЦКрЖЭЬ
	history.append(command)
	match command:
		case "help":
			print(
				"""
				Список команд:
				help - показать список команд
				whoami - вывести текущего пользователя
				echo [текст] - вывести текст в консоль
				history - вывести историю команд
				cum - ну вы поняли...
				exit - выход
				""")
			pass
		case "whoami":
			pass # Вывод текущего юзера
		case "echo":
			if (len(command) > 4):
				print(command[4:])
		case "history":
			for index, item in enumerate(history):
				print(f"{index + 1} {item}")

		case "exit":
			error_level = 1
			is_running = False
			pass
		case "cum":
			if (cum_times <= System.maxCums):
				print("cummed!")
				cum_times += 1
			else:
				print(f"You can't cum more {System.maxCums}")	
		case _:
			print(f"{command} не является действительной командой")
			

def main():
	while (is_running):
		user_input = input()




print(f"Program finished with exit code {main()}")