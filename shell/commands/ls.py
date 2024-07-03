import os

def main(*args):
    if not args or not args[0]:
        directory = os.getcwd()
    else:
        directory = args[0][0]
    
    files = os.listdir(directory)

    try:
        for file in files:
            if os.path.isdir(os.path.join(directory, file)):
                print(f"\033[1;34m{file}\033[0m")
            else:
                print(file)
    except:
        return