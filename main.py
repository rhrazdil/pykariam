# coding=utf-8

from models.pirate_fortress import PirateFortress
from models.tavern import Tavern
from time import sleep
import datetime
from utils import conf
from utils.driver import Driver
from utils.login import Login
from utils.navigator import Navigator
import random

navigator = Navigator().navigator()

driver = Driver().connect()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page and log in
driver.get(conf.site_url)
Login().log_in()

sleep(1)

pirate_fortress = PirateFortress()
navigator.navigate(pirate_fortress, 'Raid')

start = datetime.datetime.now()
while True:
    time_delta = datetime.datetime.now() - start
    if time_delta.seconds >= 8000:
        break
    try:
        pirate_fortress.raid()
    except:
        if pirate_fortress.is_captcha_displayed():
            pass
        else:
            print('Unknown error')

    while pirate_fortress.is_captcha_displayed():
        try:
            pirate_fortress.submit_captcha()
        except Exception as e:
            print(e)
            pass
        sleep(1)

    sleep(160 + random.randrange(3,35))

sleep(5)
# close the browser window
driver.quit()
