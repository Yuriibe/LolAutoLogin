import subprocess
import time
import pyperclip
import keyboard
import os

# Path to the League of Legends shortcut
shortcut_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk'

# Path to RiotClientServices.exe
riot_client_path = r'C:\Riot Games\Riot Client\RiotClientServices.exe'

program_name = "RiotClientServices.exe"

def startRiotClient():
    subprocess.Popen([shortcut_path], shell=True)

def enterLoginCredentials():
    pyperclip.copy("")
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('tab')
    time.sleep(2)
    pyperclip.copy("")
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('enter')


def is_program_running(program_name):
    try:
        # Run a command to get the list of all running processes
        output = subprocess.check_output("tasklist", shell=True).decode()
        print(output)
        # Check if the program name is in the list of running processes
        return program_name in output
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if is_program_running(program_name):
    print(f"{program_name} is running.")
else:
    print(f"{program_name} is not running.")