import subprocess
import os
import pyautogui
import webbrowser
import time

def tokenize(sentence):
    aList = []
    aWord = ""
    place = 0
    for letter in sentence:
        place += 1
        if letter != " ":
            aWord = aWord + letter.lower()
        if letter == " " or place == len(sentence):
            aList.append(aWord)
            aWord = ""  
    return aList

def tinput(command):

    if command[:5].lower() == "open ":
        command1 = command[5:]
        process = subprocess.Popen(['explorer', command1], stdout=subprocess.PIPE, universal_newlines=True)
    elif command[:6].lower() == "close ":
        command1 = command[6:]
        os.system(f"TASKKILL /F /IM {command1}.exe")
    elif command[:7].lower() == "google ":
        command1 = command[7:]

        webbrowser.open('https://google.com/?q=' + command1)
        time.sleep(1)
        pyautogui.press('enter')

#tinput(command = input("What do you want to do?\n"))
def process_input(input):
    words_list = tokenize(input)
    #if words_list[0]

print(tokenize("THIS is a TEST"))