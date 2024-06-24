import urllib.request

url            = 'https://raw.githubusercontent.com/Xuvel/Python-OS-/main/OS_VERSION.txt'

null           = "null"

github_verfile = "OS_VERSION.txt"

systemVer      = "0.0.1"
systemName     = "AAA Python OS"
maxCums        = 5

users = []


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
                    return 0x0                                     # successfull
                else:
                    return 0x1                                     # incorrect password
            else:
                self.name = newName
                return 0x0                                         # successfull
        else:
            return 0x2                                             # new name empty

                
    def setPassword(self, newPassword, *current_password) -> int:
        if (not self.password):
            if (current_password == self.password):
                self.password = newPassword
                return 0x0                                          # successful
            else:
                return 0x1                                          # incorrect password
        else:
            self.password = newPassword
            return 0x0                                              # successful
                                               
    
    def createUser(name, permission, *password) -> int:

        if (password != ""):
            return User(name, permission)
            
        else:
            return User(name, permission, password)
        
    def getPassword(username) -> str:
        return username.password

    
    def __str__(self):
        return self.name

def createFolder(name, *path):
    if (not path):
        file = open(name, 'w+')
    else:
        file = open(path+name)


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
        return None

def getOs() -> str:
    try:
        file = open('system.txt', "r")
        fileContent = file.read()
        return fileContent[12:17]
    except:
        return "file cannot be read"
