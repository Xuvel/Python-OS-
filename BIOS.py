#git-ver-1.2-alpha-test

import os
import time
import random 

def newPath(afterPath):
    return os.getcwd() + afterPath

def firstStartUp():
    if os.path.isdir(newPath("\config")):
        if os.path.isfile(newPath("\config\\bios.txt")):
            pass
        else:
            print("Файл конфигурации отсутствует, автоматическое создание.")
            open(newPath("\config\\bios.txt"), "w")
    else:
        print("Система запускается в первый раз, создание файла конфгурации.")
        os.mkdir("config")
        open(newPath("\config\\bios.txt"), "w")

class BIOS:
    def __init__(self, workDisks):
        self.workDisks = workDisks
        self.pointedDisk = 'Пусто'
        self.needStartBios = 'Пусто'
    
    def preview(self):
        print("Загрузка BIOS")
        time.sleep(3)
        if self.needBios() == True:
            print("Принудительное включение BIOS...")
            self.settings()
        elif self.osIsReady() != False:
            print(f"Запуск ОС на диске {self.pointedDisk}")
        else:
            print("Загрузочный диск не выбран или не найден")
            self.settings()

    def settings(self):
        print("===== Настройки BIOS =====")
        print()
        print(f"Принудительное включение BIOS: {self.needStartBios}")
        print(f"Диск для запуска ОС: {self.pointedDisk}")
        action = input("Изменить настройки?: ")
        if action.upper() == 'ДА':
            self.settings()



    def save_settings(self):
        while True:
            print("Для выходи из режима настройки введите \"Выход\"")
            action = input("Выберите номер настройки: ")
            if action.upper() == 'ВЫХОД':
                print("Выход из настроек.")
            elif action == '1':
                while intoaction != "ДА" or intoaction != "НЕТ":
                    intoaction = input("Переключить значение?").upper()

                if intoaction == 'ДА':
                    self.needStartBios == True
                    save_settings = open(newPath("\config\\bios.txt"), "a")
                    save_settings.write("\nTrue")
                elif intoaction == "НЕТ":
                    print("Отмена действия")

            elif action == '2':
                print("Подключенные диски:")
                print(self.workDisks)
                while intoaction not in range(len(self.workDisks)):
                    if intoaction.isdigit() == False:
                        intoaction = input("Введите ЧИСЛО.")
                    else:
                        intoaction = input("Введите номер диска для загрузки ОС: ").upper()

                self.pointedDisk = workDisks[intoaction]
                save_settings = open(newPath("\config\\bios.txt"), "a")
                save_settings.write("\nTrue")
            elif intoaction == "НЕТ":
                print("Отмена действия")

            

    def osIsReady(self):
        osIsReady = open(newPath("\config\\bios.txt"), "r")
        for i in range(len(self.workDisks)):
            if osIsReady.readline().rstrip("\n")  == self.workDisks[i]:
                self.pointedDisk = self.workDisks[i]
                return self.pointedDisk

        return False
    
    def needBios(self):
        needBios = open(newPath("\config\\bios.txt"), "r")
        self.needStartBios = needBios.readline()
        self.needStartBios = needBios.readline()
        if self.needStartBios != '':
            return self.needStartBios
        else:
            self.needStartBios = False
            return self.needStartBios
    
#print('Инициализация.', end='', flush=True)
#time.sleep(1)
#print('.', end='', flush=True)
#time.sleep(1)
#print('.', flush=True)
#print("")
if os.path.isdir(newPath("\~")): # есть ли папка ~
    disksDir = os.listdir(path=newPath("\~"))
    workDisks = []
    for i in range(len(disksDir)):
        if os.path.isfile(os.getcwd() + f"\~\{disksDir[i]}\.efi"):
            workDisks.append(disksDir[i])

firstStartUp()
bios = BIOS(workDisks)
bios.preview()
