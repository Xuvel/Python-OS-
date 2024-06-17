import os
import time
import random
import keyboard

def clear_space():
    print('\n' * 20)

def add_line():
    return ' ' * 12

def newPath(afterPath):
    return os.getcwd() + afterPath

class Disk:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def defineDisk(self):
        if self.type == 'ok':
            return 'Можно установить'
        elif self.type == 'osInstalled':
            return 'Установлена OS'
        else:
            return 'Диск поврежден'

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type


class Line:
    def __init__(self, line, pos):
        self.line = line 
        self.pos = pos
        self.num = 0

    def get_line(self):
        return self.line
    
    def get_num(self, num=0):
        self.num += num
        return self.num

    def get_pos(self):
        return self.pos


class Window:
    def __init__(self, size):
        if size == '':
            size = '39 8'
        size = size.split()
        while len(size) != 2 and all([True if i.isdigit() else False for i in size]):
            size = input('Введите длину не менее 12 и ширину не менее 8: ').split()
        self.lenght, self.width = (map(int, size))

    def append_space(self, output):
        total = []
        for i in output:
            if len(i) != self.lenght + 2:
                total.append(i[:-1] + ' ' + '|')
            else:
                total.append(i)
        return total

    def installer_window(self, lang, display):
        output = []
        surface_lay = {}
        for num in range(self.width):
            if num in display:
                line = display[num].get_line()
                pos = display[num].get_pos()
                if pos == 'centre':
                    startPrint = (self.lenght - len(line)) // 2
                    output.append('|' + ' ' * startPrint + line  + ' ' * startPrint + '|')     
                elif pos == 'left':
                    startPrint = self.lenght - len(line)
                    output.append('|' + line + ' ' * startPrint + '|')
                elif pos == 'right':
                    startPrint = self.lenght - len(line)
                    output.append('|' + ' ' * startPrint + line + '|')
                elif pos == 'list':
                    disk = line[display[num].get_num()]
                    disk_line = self.lenght - len(disk.get_name() + ': ' + disk.defineDisk()) - 1
                    output.append('| ' + disk.get_name() + ': ' + disk.defineDisk() + ' ' * disk_line + '|')
                    startPrint = (self.lenght - 1) // 2
                    if num != 0 and display[num].get_num() > 0:
                        surface_lay[num - 1] = '| ' + ' ' * startPrint + '▲' + ' ' * startPrint + '|'
                    if num != self.width and display[num].get_num() < len(line) - 1:
                        surface_lay[num + 1] = '| ' + ' ' * startPrint + '▼' + ' ' * startPrint + '|'
            else:
                output.append('|' + ' ' * self.lenght + '|')
        output = self.append_space(output)
        decor = '<' + ''.join(['=' if i % 2 == 0 else '-' for i in range(self.lenght)]) + '>'
        print('                TripleOS\n' + decor)
        for i in range(len(output)):
            if i in surface_lay:
                print(''.join([surface_lay[i][j] if surface_lay[i][j] != ' ' else output[i][j] for j in range(len(output[i]))]))
            else:
                print(output[i])
        print(decor)


class Installer:
    def __init__(self, window):
        self.lang = 'ru'
        self.window = window

    def set_lang(self, lang):
        self.lang = lang

    def installBoot(self):
        workDisks = []     
        disksDir = os.listdir(path=newPath("\~"))
        for i in range(len(disksDir)):
            if os.path.isfile(os.getcwd() + f"\~\{disksDir[i]}\.efi"):
                if os.path.isfile(os.getcwd() + f"\~\{disksDir[i]}\os.txt"):
                    workDisks.append(Disk(disksDir[i], 'osInstalled'))
                else:
                    workDisks.append(Disk(disksDir[i], 'ok'))
        window.installer_window(self.lang, {1: Line('Installation location', 'centre'), 4: Line(workDisks, 'list'), 7: Line('Confirm', 'centre')})
        

window = Window(input('Введите длину и ширину окна через пробел (необязательно): '))
installer = Installer(window)
installer.installBoot()