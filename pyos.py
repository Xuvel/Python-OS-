import time
import os
from sys import platform

import System

global error_level, working
error_level = 0x0
working = True

'''
0 default exit
1 restarting
2 unknown error
3 system cannot be initialized
4 can not read config.txt
'''

def mainDir():
	return os.getcwd()

def getOSType():
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "OS X"
    elif platform == "win32":
        return "windows"
    else:
        working = False
        error_level = hex(3)
        return False

def main():
	global error_level
	system = System(getOSType())
	print(f"System type -", system.getType())
	print(f"Main directory - {__file__}")
	try:
		os.makedirs("System/configs")
		config = open("System/configs/config.txt", "w")
		config.write("language = en")
		error_level = 0x1
	except IOError:
		try:
			file = open(f"{mainDir()}/System/configs/config.txt", "r")
			content = file.read()
			print(content)
		except IOError:
			print("Can not read config.txt file")
			error_level = 0x4
	print(f"{mainDir()}/System/configs/config.txt")
	print("System is starting")
	return error_level


print(f'Program finished with exit code {hex(main())}')