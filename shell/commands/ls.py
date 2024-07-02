import os

def main():
    files = os.listdir()

    for file in files:
        if os.path.isdir(file):
            print(f"\033[1;34m{file}\033[0m")
        else:
            print(file)