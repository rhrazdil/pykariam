# coding=utf-8

from models.pirate_fortress import PirateFortress
from models.tavern import Tavern
from time import sleep
from utils import conf
from utils.driver import Driver
from utils.login import Login
from utils.navigator import Navigator


navigator = Navigator().navigator()

driver = Driver().connect()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page and log in
driver.get(conf.site_url)
Login().log_in()

tavern = Tavern()
tavern.set_max_consumption()

pirate_fortress = PirateFortress()
pirate_fortress.launch_raid()

sleep(5)
# close the browser window
driver.quit()
