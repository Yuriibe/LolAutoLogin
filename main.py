import pygetwindow as gw
from programmController import *
from loginController import *

leagueClient = "LeagueClient.exe"
riotClient = "RiotClientServices.exe"


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
            winLeague = gw.getWindowsWithTitle('League Of Legends')[0]
            winLeague.close()
            kill_process(riotClient)
        startRiotClient()
        time.sleep(5)
        enterLoginCredentials()
        print(f"{riotClient} is not running.")

main()