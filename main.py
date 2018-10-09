# coding=utf-8

from models.pirate_fortress import PirateFortress
from models.tavern import Tavern
from models.city import City
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


import IPython;IPython.embed()

start = datetime.datetime.now()
while True:
    time_delta = datetime.datetime.now() - start
    if time_delta.seconds >= 20000:
        pass

    pirate_fortress.raid()
    sleep(155 + random.randrange(3,10))


# close the browser window
driver.quit()
