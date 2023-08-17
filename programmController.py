import subprocess
import os

shortcut_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk'

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

def startRiotClient():
        subprocess.Popen([shortcut_path], shell=True)
