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

pirate_fortress = PirateFortress()
navigator.navigate(pirate_fortress, 'All')

start = datetime.datetime.now()
while True:
    time_delta = datetime.datetime.now() - start
    if time_delta.seconds >= 8000:
        break

    pirate_fortress.raid()

    sleep(155 + random.randrange(3,20))

sleep(5)
# close the browser window
driver.quit()
