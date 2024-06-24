print("""
~~~~~TripleOS calculator~~~~~
Введите выражение, либо выполните команду.

Доступные команды:
exit/e - выход
""")

while True:
    command = str(input("> "))
    if command.lower() == "exit" or command.lower() == "e":
        print("Работа программы завершена")
        break
    try:
        print(eval(command))
    except:
        print("Ошибка!")