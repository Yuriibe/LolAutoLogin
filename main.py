import pygetwindow as gw
from programmController import *
from loginController import *
import tkinter

leagueClient = "LeagueClient.exe"
riotClient = "RiotClientServices.exe"


def main():
    if is_program_running(riotClient) and not is_program_running(leagueClient):
        loginData = getUserData()
        print(f"{riotClient} is running.")
        try:
            winRiot = gw.getWindowsWithTitle('Riot Client')[0]
            winRiot.activate()
            enterLoginCredentials(loginData)
        except:
            kill_process(riotClient)
            main()
    else:
        loginData = getUserData()
        if is_program_running(leagueClient):
            winLeague = gw.getWindowsWithTitle('League Of Legends')[0]
            winLeague.close()
            kill_process(riotClient)
        startRiotClient()
        time.sleep(5)
        enterLoginCredentials(loginData)
        print(f"{riotClient} is not running.")


if __name__ == "__main__":
    main()
