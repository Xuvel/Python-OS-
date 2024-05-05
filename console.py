import os
import time
import subprocess

def mainDir():
	return os.getcwd()

if (os.name == "nt"):
	
	clear = lambda: os.system('cls')
else:
	clear = lambda: os.system('clear')
command_list = ["help", "stop"]
version = "v.0.1"
stop = False
user_input = ""
error_level = 0x00000

def loading(times, text, wait):
	for i in range(times):
		print(f"loading [|]{text}")
		time.sleep(wait)
		clear()
		print(f"loading [/]{text}")
		time.sleep(wait)
		clear()
		print(f"loading [-]{text}")
		time.sleep(wait)
		clear()
		print(f"loading [\\]{text}")
		time.sleep(wait)
		clear()

def check(command):
	global stop
	match command:
		case "help":
			print("help-\nstop-\nstart-\noutput-\nsystem(X)-")
			
		case "stop":
			stop = True
			print("stop")
			global error_level
			error_level = 0x00001
		case "":
			print(f"Command for help using \"help\"")
		case "system(z)":
			stop = True
			error_level = 0x00002
		case "error list":
			print("0x00001 - user exit\n0x00002 - unknown error")
		case "start":
			subprocess.call(["python", "newfile.py"])
		case _:
			if (command[:6] == "output"):
				if (len(command) > 7):
					print(command[7:])
				else:
					print("syntax error", end = "")
			else:
				print(f"Unknown command \"{command}\"")

print(f"Triple A DOS {version}")		
def main():
	time.sleep(0)
	loading(4, "", 0)
	print("Triple A OS console")
	while (stop == False):
		print(">>", end = "")
		user_input = input()
		check(user_input)
	return error_level
	
print(f"Program finished with exit code {hex(main())}")
	