# coding=utf-8

from utils.login import Login
from utils.driver import Driver
from utils import conf
from utils.navigator import Navigator
from models.pirate_fortress import PirateFortress
from models.tavern import Tavern

navigator = Navigator().navigator()

driver = Driver().connect()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page and log in
driver.get(conf.site_url)
Login().log_in()

tavern = Tavern()
tavern.set_max_consumption()
# close the browser window
driver.quit()
