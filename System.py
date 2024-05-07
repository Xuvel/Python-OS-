import os

import urllib.request
url = 'https://raw.githubusercontent.com/Xuvel/Python-OS-/main/OS_VERSION.txt'


github_verfile = "OS_VERSION.txt"

systemVer      = "0.0.1"
systemName     = "AAA Python OS"

def get_ver():
    return systemVer

def get_name():
    return systemName

def get_last_version():
    try:
        filename = github_verfile
        urllib.request.urlretrieve(url, filename)
        file = open(filename, "r")
        fileContent = file.read()
        return fileContent
    except:
        return "null"
        


print(get_last_version())