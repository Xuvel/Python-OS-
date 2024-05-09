import os

import urllib.request
url = 'https://raw.githubusercontent.com/Xuvel/Python-OS-/main/OS_VERSION.txt'

null = "null"

github_verfile = "OS_VERSION.txt"

systemVer      = "0.0.1"
systemName     = "AAA Python OS"


class User:
    def __init__(self, name, permissions, *password):
        self.name        = name
        self.permissions = permissions
        self.password    = password

    def changeName(self, newName, *password) -> int:
        if (newName != ""):
            if (self.password != ""):
                if (self.password == password):
                    self.name = newName
                    return 0x0 # successfull
                else:
                    return 0x1 # incorrect password
            else:
                self.name = newName
                return 0x0     # successfull
        else:
            return 0x2         # new name empty

                
    def setPassword(self, newPassword, *current_password) -> int:
        if (not self.password):
            if (current_password == self.password):
                self.password = newPassword
                return 0x0                                          # successful
            else:
                return 0x1                                          # incorrect password
        else:
            self.password = newPassword
            return 0x0                                              # new password
                                               # successful
    
    def createUser(name, permission, *password) -> int:

        if (password != ""):
            return User(name, permission)
        else:
            return User(name, permission, password)
        


def getVersion() -> str:
    return systemVer

def getName() -> str:
    return systemName

def getLastVersion() -> str:
    try:
        filename = github_verfile
        urllib.request.urlretrieve(url, filename)
        file = open(filename, "r")
        fileContent = file.read()
        return fileContent
    except:
        return null
    


print(getLastVersion())