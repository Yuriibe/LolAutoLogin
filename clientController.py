import pygetwindow as gw
from programmController import *
from loginController import *

leagueClient = "LeagueClient.exe"
riotClient = "RiotClientServices.exe"

def main(slectedIndex):
    if slectedIndex is not None:
        if is_program_running(riotClient) and not is_program_running(leagueClient):
            loginData = getUserData(slectedIndex)
            print(f"{riotClient} is running.")
            try:
                winRiot = gw.getWindowsWithTitle('Riot Client')[0]
                winRiot.activate()
                enterLoginCredentials(loginData)
            except:
                kill_process(riotClient)
                main(slectedIndex)
        else:
            loginData = getUserData(slectedIndex)
            if is_program_running(leagueClient):
                winLeague = gw.getWindowsWithTitle('League Of Legends')[0]
                winLeague.close()
                kill_process(riotClient)
            startRiotClient()
            time.sleep(5)
            enterLoginCredentials(loginData)
            print(f"{riotClient} is not running.")


