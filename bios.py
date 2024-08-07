import os
import time
import sys
import json

def newPath(afterPath): # Возвращает текущий путь к файлу bios.py + путь в аргументах
    return os.getcwd() + afterPath

def separateFile(path):
    return path.strip('\n')

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def firstStartUp(): # Проверка существования папки config и файла bios.json
    if not os.path.isdir(newPath("/config")):
        print("Система запускается в первый раз, создание файла конфгурации.")
        os.mkdir(newPath("/config"))
    if not os.path.isfile(newPath("/config/bios.json")):
        print("Файл конфигурации отсутствует, автоматическое создание.")
        with open(newPath("/config/bios.json"), "w", encoding="utf-8") as new_file:
            json.dump(
                {
                    "bios_autostart": True,
                    "startup_disk": None
                }, new_file
            )
    if not os.path.isdir(newPath("/disks")):
        os.mkdir(newPath("/disks"))

class BIOS:
    def __init__(self, workDisks):
        self.workDisks = workDisks
        self.disabledDisks = []
        self.local = {False: 'Нет', True: 'Да'}
        
    def preview(self): 
        """
        Загрузка Биоса и переход к загрузке ОС. 
        Настройки: 1 - Принудительное включение настроек биоса, 
        2 - Проверка доступности выбранного диска
        """
        while True:
            clearConsole()
            try:
                print("Загрузка BIOS")
                time.sleep(3)
            except (KeyboardInterrupt, EOFError):
                print('Выход в меню настроек...')
                time.sleep(1)
                self.settings()
                continue
            if self.needBios() == True: # Проверка настройки №1
                print("Принудительное включение BIOS...")
                time.sleep(1)
                self.settings()
            elif self.diskIsReady() != "Пусто": # Проверка настройки №2
                print(f"Запуск ОС на диске {self.diskIsReady()}")
                if self.runOS(): # True - выход в настройки, False - прекращение работы
                    print('Выход в меню настроек...')
                    time.sleep(2)
                    self.settings()
                else:
                    break
            else:
                time.sleep(2)
                print("Загрузочный диск не выбран или не найден")
                print('Выход в меню настроек...')
                self.settings()

    def settings(self): 
        """
        Вывод информации настроек и переход к изменению настроек (save_settings) и управлению дисками (disks_settings)
        """
        while True:
            clearConsole()
            print("======== Настройки BIOS ========")
            print('  Диски  |  Настройка  |  Выход ')
            print()
            print(f"Принудительное включение BIOS: {self.local[self.needBios()]}")
            print(f"Диск для запуска ОС: {self.diskIsReady()}")
            action = ''
            print('--------------------------------')
            while action not in ['1', '2', '3']: # Выбор раздела настроек
                print('Для переключения между разделами настроек введите номер раздела')
                action = input("Введите номер раздела настроек: ").upper()
                if action == '1':
                    self.disks_settings()
                
                elif action == '2':
                    self.save_settings()

                elif action == '3':
                    return None

    def save_settings(self): 
        """
        Режим изменения настроек. Сохраняет изменения в файл bios.json
        """
        while True:
            clearConsole()
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print(f"1) Принудительное включение BIOS: {self.local[self.needBios()]}")
            print(f"2) Диск для запуска ОС: {self.diskIsReady()}")
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            try:
                print(output)
            except UnboundLocalError:
                pass
            print("Для выхода из режима настройки введите \"Выход[в]/exit[e]\"")
            action = input("Выберите номер настройки: ")
            if action.upper() in ["ВЫХОД", "В", "EXIT", "E"]:
                print("Выход из настроек.")
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                break
            elif action == '1': # Настройка №1. Принудительное включение BIOS.
                action = ''
                while action not in ['ДА', 'Д', 'НЕТ', 'НЕ', 'Н', 'Y', 'N']:
                    action = input("Переключить значение? \"да[д]/нет[н]\": ").upper()

                if action in ['ДА', 'Д', 'Y']:
                    with open(newPath("/config/bios.json"), "r+") as save_settings:
                        bios_config = json.load(save_settings)
                        save_settings.seek(0)
                        save_settings.truncate(0)
                        if bios_config["bios_autostart"] == False:
                            bios_config["bios_autostart"] = True
                        else:
                            bios_config["bios_autostart"] = False
                        json.dump(bios_config, save_settings)
                    output = f'Значение изменено на {self.local[self.needBios()]}'

                elif action in ['НЕТ', 'НЕ', 'Н', 'N']:
                    print("Отмена действия")

            elif action == '2': # Настройка №2. Выбор диска для запуска ОС
                if len(self.workDisks) != 0:
                    print("Подключенные диски:")
                    for i in range(len(self.workDisks)):
                        print(f'{i + 1}) {self.workDisks[i]}')
                    action = '0'
                    while action not in [str(i) for i in range(1, len(self.workDisks) + 1)]:
                        if action.upper() in ['ВЫХОД', 'В']:
                            return None
                        else:
                            action = input("Введите номер диска для загрузки ОС: ").upper()

                    with open(newPath("/config/bios.json"), "r+") as save_settings:
                        save = json.load(save_settings)
                        save["startup_disk"] = self.workDisks[int(action) - 1]
                        save_settings.seek(0)
                        save_settings.truncate(0)
                        json.dump(save, save_settings)

                    output = f'Значение изменено на {self.diskIsReady()}'
                else:
                    print("Не найдено ни одного диска!")

    def disks_settings(self): 
        """
        Режим изменения дисков. Создает/отключает/удаляет диски.
        """
        pathToSystem = f'/disks/'
        while True:
            clearConsole()
            print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('ЭТА ФУНКЦИЯ ДЛЯ **РАЗРАБОТЧИКОВ**! В ОРИГИНАЛЕ ЭТОГО РАЗДЕЛА НЕ ДОЛЖНО БЫТЬ, Т.К. ЭТО НЕ РЕАЛИСТИЧНО!')
            print('Все подключенные диски:')
            if len(self.workDisks) == 0:
                print('Ни одного диска не найдено!')
            for i in range(len(self.workDisks)):
                status = 'Занят' if os.path.isfile(newPath(f"/disks/{self.workDisks[i]}/os.txt")) else 'Пуст'
                print(f'{i + 1}) {self.workDisks[i]}: {status}')

            print('------------------------------------------------')
            print('| Создать диск | Отключить диск | Удалить диск |')
            print('------------------------------------------------')

            try:
                print(output)
            except UnboundLocalError:
                pass
            action = input('Выберите раздел: ').upper()

            if action == '1': # Создание диска
                action = input('Название диска: ')
                real_name = action.replace(' ', '')
                os.mkdir(newPath(pathToSystem + real_name))
                with open(newPath(pathToSystem + real_name + '/.efi'), "w") as efi:
                    pass
                output = 'Диск создан'

            elif action == '2': # Отключение диска
                print('После отключения диска, он пропадет из списка выбора и заработает только после перезапуска Биоса')
                action = ''
                while action not in [str(i) for i in range(1, len(self.workDisks) + 1)]:
                    action = input('Выберите диск: ')
                self.disabledDisks.append(self.workDisks[int(action) - 1])
                output = 'Диск отключен'

            elif action == '3': # Удаление диска
                print('Работает только с правами администратора!')
                action = ''
                while action not in [str(i) for i in range(1, len(self.workDisks) + 1)]:
                    action = input('Выберите диск: ')
                try:
                    os.remove(newPath(pathToSystem + self.workDisks[int(action) - 1]))
                    output = 'Диск удален'
                except PermissionError:
                    output = 'Отказано в доступе. Запустите Биос через командную строку с правами администратора и повторите попытку.'
            elif action in ['ВЫХОД', 'В']:
                return None
            self.workDisks = [i for i in scan_disks() if i not in self.disabledDisks]
            print('--------------------------------')
        
    def runOS(self): # Запуск ОС. Возвращает True или False
        pathToSystem = f'/disks/{self.diskIsReady()}/'
        sys.path.insert(1, newPath(pathToSystem))
        fileDir = [i for i in os.listdir(newPath(pathToSystem)) if i.endswith('.py')]
        toDel = []
        for i in fileDir: 
            """
            Проверка файлов .py на диске. Отсеевает файлы не-загрузчики, оставляет загрузчики. 
            Загрузчиком считается тот файл, в котором есть функция startUp (это функция, которая запускает саму ОС)
            """
            try:
                checking = __import__(i[:-3], globals(), locals(), ['startUp'])
                if 'startUp' not in dir(checking):
                    raise AttributeError
            except AttributeError:
                toDel.append(i)
        fileDir = [i for i in fileDir if i not in toDel]

        if len(fileDir) == 0:
            print('Ни одного диска не найдено!')
            return True
        elif len(fileDir) > 1: # Выбор загрузчика, если их больше одного
            print('На диске присутствует несколько файлов загрузки.')
            print('Для отмены введите "Выход"')
            for i in range(len(fileDir)):
                with open(newPath(pathToSystem + fileDir[i]), "r") as show_file:
                    show = show_file.readlines()[0]
                print(f'{i + 1}) {show[1:].strip()} ({fileDir[i]})')
            action = '0'
            while action.upper() not in [str(i) for i in range(1, len(fileDir) + 1)] + ['ВЫХОД']:
                action = input("Введите номер файла: ").upper()
            if action.isdigit():
                action = int(action) - 1
            else:
                return True
        else:
            action = 0

        print(f'Запуск {fileDir[action][:-3]}')
        start = __import__(fileDir[action][:-3])
        start.startUp()
        return False

    def needBios(self): # Проверка необходимости включения Биоса, указанного в строке bios.json. Возвращает F или T (True или False)
        with open(newPath("/config/bios.json"), "r") as needBios:
            need = json.load(needBios)
            return need["bios_autostart"]

    def diskIsReady(self): # Проверка доступности диска, указанного в первой строке bios.json. Возвращает название диска
        with open(newPath("/config/bios.json"), "r") as needDisk:
            need = json.load(needDisk)
            for i in self.workDisks:
                if need["startup_disk"] == i and need["startup_disk"] != None:
                    return i
        return 'Пусто'

def scan_disks():
    workDisks = []     
    if os.path.isdir(newPath("/disks")): # Проверка существования папки disks и поиск дисков
        disksDir = os.listdir(path=newPath("/disks"))
        for i in range(len(disksDir)):
            if os.path.isfile(os.getcwd() + f"/disks/{disksDir[i]}/.efi"):
                workDisks.append(disksDir[i])
    return workDisks

firstStartUp()
bios = BIOS(scan_disks())
bios.preview()