def main(*args):
    if not args or not args[0]:
        print("Аргумент [file] является обязательным")
        return
    else:
        file = args[0][0]

    try:
        with open(file, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла '{file}': {e}")