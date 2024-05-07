import os
import requests

user = str(os.getusername())

url = 'https://raw.githubusercontent.com/Xuvel/Python-OS-/main/pyos.py' 
r = requests.get(url, allow_redirects=True)
fpath = "C:\Users\\" + user + "\AppData\Roaming\\"

def main():
    if (os.path.exists(f"C:\Users\{user}\AppData\Roaming\pyos\pyos.py")):
        return 0x0
    else:
        try:
            os.mkdir(f"C:\Users\{user}\AppData\Roaming\pyos")
        except:
            return 0x2
        try:
            open('pyos.py', 'wb').write(r.content)
        except:
            return 0x3
error_level = main()

prtin("py os is installed") if (error_level == 0x0) else print("installing") if (error_level == 0x1) else print("directory cannot be created") if (error_level == 0x2) else print("file cannot be created/downloaded") if (error_level == 0x3) else print("os cannot be install")

print(f"error {error_level}")