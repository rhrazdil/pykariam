# coding=utf-8

from login import Login
from utils.driver import Driver
import conf

driver = Driver().connect()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page and log in
driver.get(conf.site_url)
Login().log_in()


# close the browser window
driver.quit()
