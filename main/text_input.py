import subprocess
import os
def tinput(command):
    if command[:5] == "open ":
        command1 = command[5:]
        process = subprocess.Popen(['explorer', command1], stdout=subprocess.PIPE, universal_newlines=True)
    elif command[:6] == "close ":
        command1 = command[6:]
        os.system(f"TASKKILL /F /IM {command1}.exe")
    else:
        print('no')

tinput(command = input("text\n"))