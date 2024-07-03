import os

def main(*args):
    if not args or not args[0]:
        print("Аргумент [file] является обязательным")
        return
    else:
        file = args[0][0]

    try:
        os.remove(file)
        print(f"Файл '{file}' успешно удалён")
    except OSError as e:
        print(f"Ошибка при удалении файла '{file}': {e}")
    except Exception as e:
        print(f"Не удалось удалить файл '{file}': {e}")