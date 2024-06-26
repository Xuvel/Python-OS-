import os
import time

def newPath(afterPath): # Возвращает текущий путь к файлу BIOS.py + путь в аргументах
    return os.getcwd() + afterPath 

def separateFile(path):
    return path.strip('\n')

def firstStartUp(): # Проверка существования папки config и файла bios.txt
    if not os.path.isdir(newPath("\config")):
        print("Система запускается в первый раз, создание файла конфгурации.")
        os.mkdir("config")
    if not os.path.isfile(newPath("\config\\bios.txt")):
        print("Файл конфигурации отсутствует, автоматическое создание.")
        with open(newPath("\config\\bios.txt"), "w") as new_file:
            new_file.write('T\nNone')

class BIOS:
    def __init__(self, workDisks):
        self.workDisks = workDisks
        self.pointedDisk = 'Пусто'
        self.needStartBios = 'Пусто'
        self.local = {'F': 'Нет', "T": 'Да'}
        
    def preview(self): # Загрузка Биоса и переход к загрузке ОС
        while True:
            print("Загрузка BIOS")
            time.sleep(3)
            if self.needBios() == "T":
                print("Принудительное включение BIOS...")
                self.settings()
            elif self.osIsReady() != False:
                print(f"Запуск ОС на диске {self.pointedDisk}")
            else:
                print("Загрузочный диск не выбран или не найден")
                self.settings()

    def settings(self): # Выведение информации настроек и переход к изменению настроек (save_settings)
        while True:
            print("======== Настройки BIOS ========")
            print('    Настройка    |     Выйти    ')
            print()
            print(f"Принудительное включение BIOS: {self.local[self.needBios()]}")
            print(f"Диск для запуска ОС: {self.pointedDisk}")
            action = ''
            print('--------------------------------')
            while action not in ['1', '2', '3']: # Выбор раздела настроек
                print('Для переключения между разделами введите номер раздела')
                action = input("Введите номер раздела: ").upper()
                if action == '1':
                    self.save_settings()
                
                if action == '2':
                    return None

    def save_settings(self): # Режим изменения настроек. Сохраняет изменения в файл bios.txt
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f"1) Принудительное включение BIOS: {self.local[self.needBios()]}")
        print(f"2) Диск для запуска ОС: {self.pointedDisk}")
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print("Для выхода из режима настройки введите \"Выход\"")
        while True:
            action = input("Выберите номер настройки: ")
            if action.upper() == 'ВЫХОД':
                print("Выход из настроек.")
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                break
            elif action == '1': # Настройка №1. Принудительное включение BIOS.
                action = ''
                while action != 'ДА' and action != 'НЕТ':
                    action = input("Переключить значение? ").upper()

                if action == 'ДА':
                    with open(newPath("\config\\bios.txt"), "r+") as save_settings:
                        save = save_settings.readlines()
                        save_settings.seek(0)
                        if separateFile(save[0]) == "F":
                            save[0] = "T\n"
                        else:
                            save[0] = "F\n"
                        save_settings.writelines(save)

                    print(f'Значение изменено на {self.local[self.needBios()]}')

                elif action == "НЕТ":
                    print("Отмена действия")

            elif action == '2': # Настройка №2. Выбор диска для запуска ОС
                if len(workDisks) != 0:
                    print("Подключенные диски:")
                    for i in range(len(workDisks)):
                        print(f'{i + 1}) {workDisks[i]}')
                    action = '0'
                    while action not in [str(i) for i in range(1, len(self.workDisks) + 1)]:
                        if action.isdigit() == False:
                            action = input("Введите ЧИСЛО: ").upper()
                        else:
                            action = input("Введите номер диска для загрузки ОС: ").upper()

                    self.pointedDisk = workDisks[int(action) - 1]
                    with open(newPath("\config\\bios.txt"), "r+") as save_settings:
                        save = save_settings.readlines()
                        save_settings.seek(0)
                        save[1] = self.pointedDisk
                        save_settings.writelines(save)

                    print(f'Значение изменено на {self.pointedDisk}')

                else:
                    print("Не найдено ни одного диска!")

            elif action == '3':
                pass

    def osIsReady(self): # Проверка доступности диска, указанного в первой строке bios.txt. Возвращает название диска
        osIsReady = open(newPath("\config\\bios.txt"), "r")
        needDisk = osIsReady.readlines()
        for i in range(len(self.workDisks)):
            if separateFile(needDisk[1]) == self.workDisks[i] and separateFile(needDisk[1]) != 'None':
                self.pointedDisk = self.workDisks[i]
                return self.pointedDisk
        return False
    
    def needBios(self): # Проверка необходимости включения Биоса, указанного в строке bios.txt. Возвращает F или T (True или False)
        needBios = open(newPath("\config\\bios.txt"), "r")
        self.needStartBios = needBios.readline()
        if self.needStartBios == 'None':
            self.needStartBios = "F"
        return separateFile(self.needStartBios)

workDisks = []     
if os.path.isdir(newPath("\disks")): # Проверка существования папки ~ 
    disksDir = os.listdir(path=newPath("\disks"))
    for i in range(len(disksDir)):
        if os.path.isfile(os.getcwd() + f"\disks\{disksDir[i]}\.efi"):
            workDisks.append(disksDir[i])

firstStartUp()
bios = BIOS(workDisks)
bios.preview()