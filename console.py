import os
import time
import subprocess

import System

def mainDir():
	return os.getcwd()

if (os.name == "nt"):
	
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')
command_list = ["help", "stop"]
version = "v.0.1"
isRunning = True
user_input = ""
error_level = 0x0

def check(command):
	
	global isRunning

	print(command[7:14])

	if (command == "exit"):
		isRunning = False

	if (len(command) >= 2):
		if (command[:2] == "do"):
			
			if (command[3:7] == "get-"):

				if (command[7:20] == "-current_ver"):
					print(System.getLastVersion())
				elif (command[7:15] == "-os_ver"):
					print(System.getVersion())
				elif (command[7:16] == "-os_name"):
					print(System.getName())
				elif (command[7:18] == "-user_name"):
					print()
				elif (command[7:11] == "-os"):
					print(System.getOs())
			
			elif (command[3:10] == "create-"):
				if (command[10:15] == "-user"):
					name = input("type a name: ")
					if (name != ""):
						permissions = input("type a type of permission (ADM or USER): ")
						if (permissions == "ADM" or permissions == "USER"):
							password = input("type a password: ")
							if (password != ""):
								return None
								# eval(name) = System.User.createUser(name, permissions, password)
							else:
								return None
								# newUser = System.User.createUser(name, permissions)
						else:
							print("incorrect permission type")
					else:
						print("name is empty")

			elif (command[3:7] == "set-"):
				if (command[7:14] == "-name"):

					print("successful") if (newUser.changeName(command[14:]) == 0x0) else print("incorrect password") if (newUser.changeName(command[14:]) == 0x1) else print("unknown")



print(f"Triple A DOS {version}")		
def main():
	time.sleep(0)
	print("Triple A OS console")
	while (isRunning):
		print(f"{mainDir()} $ ", end = "")
		user_input = input()
		check(user_input)
	return error_level
	
print(f"Program finished with exit code {hex(main())}")
