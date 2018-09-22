# coding=utf-8

from selenium import webdriver
from login import Login

import conf

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page
driver.get(conf.site_url)

login = Login(driver)
login.log_in()

# close the browser window
driver.quit()
