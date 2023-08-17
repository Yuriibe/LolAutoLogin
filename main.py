import subprocess
import time
import pyperclip
import keyboard
import pygetwindow as gw
import os

# Path to the League of Legends shortcut
shortcut_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk'

# Path to RiotClientServices.exe
riot_client_path = r'C:\Riot Games\Riot Client\RiotClientServices.exe'
leagueClient = "LeagueClient.exe"
riotClient = "RiotClientServices.exe"


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
        # Check if the program name is in the list of running processes
        return program_name in output
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def kill_process(process_name):
    os.system(f"taskkill /f /im {process_name}")




def main():
    if is_program_running(riotClient) and not is_program_running(leagueClient):
        print(f"{riotClient} is running.")
        try:
            winRiot = gw.getWindowsWithTitle('Riot Client')[0]
            winRiot.activate()
            enterLoginCredentials()
        except:
            kill_process(riotClient)
            main()
    else:
        if is_program_running(leagueClient):
            win = gw.getWindowsWithTitle('League Of Legends')[0]
            win.close()
            kill_process(riotClient)
        startRiotClient()
        enterLoginCredentials()
        print(f"{riotClient} is not running.")

main()