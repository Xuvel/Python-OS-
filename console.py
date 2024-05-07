import os
import time
import subprocess

import System

def mainDir():
	return ""

if (os.name == "nt"):
	
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')
command_list = ["help", "stop"]
version = "v.0.1"
stop = False
user_input = ""
error_level = 0x00000

def check(command):
	
	global stop

	print(command[7:15])

	if (command == "stop"):
		stop = True

	if (len(command) >= 2):
		if (command[:2] == "do"):
			
			if (command[3:7] == "get-"):

				if (command[7:19] == "-currentVer"):
					print(System.get_last_version())
				elif (command[7:15] == "-os_ver"):
					print(System.get_ver())
				elif (command[7:16] == "-os_name"):
					print(System.get_name())



print(f"Triple A DOS {version}")		
def main():
	time.sleep(0)
	print("Triple A OS console")
	while (stop == False):
		print(">>", end = "")
		user_input = input()
		check(user_input)
	return error_level
	
print(f"Program finished with exit code {hex(main())}")
