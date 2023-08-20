from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.parse
from loginData import userData
from selenium.webdriver.common.by import By



def getRank(encoded_summoner_name):
    browser.get('https://www.op.gg/summoners/euw/'+encoded_summoner_name)
    try:
        rank = browser.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/div[1]/div/span')
    except NoSuchElementException:
        try:
            rank = browser.find_element(By.XPATH, '//*[@id="content-container"]/div[1]/div[1]/div[2]/div[2]/div[1]')
        except NoSuchElementException:
            rank = None
    if rank:
        return rank.text
    else:
        print("Rank not found")

for account in userData:
    browser = webdriver.Firefox()
    encoded_summoner_name = urllib.parse.quote(account['ign'], encoding='utf-8')
    account['rank'] = getRank(encoded_summoner_name)
    browser.quit()

with open('loginData.py', 'w',encoding='utf-8') as file:
    file.write("userData = " + repr(userData))