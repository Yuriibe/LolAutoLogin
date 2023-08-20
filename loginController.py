import pyperclip
import keyboard
import time
import os
from loginData import userData


def enterLoginCredentials(loginData):
    pyperclip.copy(loginData['username'])
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('tab')
    time.sleep(2)
    pyperclip.copy(loginData['password'])
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('enter')


def getUserData(accountId):
    if os.path.isfile("loginData.py"):
            return userData[int(accountId)]
    else:
        print("doesnt exist")
        with open("loginData.py", "w") as file:
            pass
