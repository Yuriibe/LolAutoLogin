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

def getUserData():
    if os.path.isfile("loginData.py"):
        for index, data in enumerate(userData):
            username = data["username"]
            print(f"{index} : Username: {username}")
        accountId = input("which Account you wanna use your Chair on: ")
        return userData[int(accountId)]
    else:
        print("doesnt exist")
        with open("loginData.py", "w") as file:
            pass

