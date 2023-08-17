import pyperclip
import keyboard
import time

from loginData import userData

def enterLoginCredentials():
    pyperclip.copy(userData[0]["username"])
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('tab')
    time.sleep(2)
    pyperclip.copy(userData[0]["password"])
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('enter')