import os

def main(*args):
    if not args or not args[0]:
        print("Аргумент [directory] является обязательным")
        return
    else:
        directory = args[0][0]

    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"Директория '{directory}' не существует.")
    except Exception as e:
        print(f"Не удалось изменить директорию '{directory}': {e}")