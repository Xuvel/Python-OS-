def main(*args):
    if not args or not args[0]:
        print("Аргумент [file] является обязательным")
        return
    else:
        file = args[0][0]

    try:
        with open(file, "w", encoding="utf-8") as file:
            print(f"Файл '{file.name}' успешно создан")
    except Exception as e:
        print(f"Ошибка при создании файла '{file}': {e}")