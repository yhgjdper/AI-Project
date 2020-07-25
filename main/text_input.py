import subprocess
import os
<<<<<<< HEAD
=======
import pyautogui
import webbrowser
import time
>>>>>>> ae948d2852e278e09de6b7d6c786f44eb405a3e2

def tinput(command):
    if command[:5] == "open " or command[:5] == "Open ":
        command1 = command[5:]
        process = subprocess.Popen(['explorer', command1], stdout=subprocess.PIPE, universal_newlines=True)
    elif command[:6] == "close " or command[:6] == "Close ":
        command1 = command[6:]
        os.system(f"TASKKILL /F /IM {command1}.exe")
    elif command[:7] == "google " or command[:7] == "Google ":
        command1 = command[7:]

        webbrowser.open('https://google.com/?q=' + command1)
        time.sleep(1)
        pyautogui.press('enter')

tinput(command = input("What do you want to do?\n"))