from googletrans import Translator
# Для установки этой библиотеки нужно выполнить эту команду:
# pip install googletrans==4.0.0-rc1

translator = Translator()

src_lang = "ru"
dest_lang = "en"

print("""
~~~~~TripleOS translator~~~~~
Введите предложение, либо выполните команду.

Доступные команды:
lang/l - выбор языков
exit/e - выход
""")

while True:
    command = str(input(f"{src_lang} → {dest_lang}> "))
    if command.lower() == "exit" or command.lower() == "e":
        print("Работа программы завершена")
        break

    elif command.lower() == "lang" or command.lower() == "l":
        try:
            print("Выбор языков\nВводите язык в формате ru, en...")

            src_lang = input("Введите язык, с которого перевести текст: ")
            dest_lang = input("Введите язык, на который перевести текст: ")
            print("✔ Применено")
        except:
            print("✖ Ошибка! Неверный формат языка!")

        continue

    try:
        result = translator.translate(command, src=src_lang, dest=dest_lang)
        print(f">>> {result.text}")
    except:
        print("Ошибка перевода!")