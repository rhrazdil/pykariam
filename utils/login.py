from utils import conf
import credentials
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from utils.driver import Driver


class Login(object):
    def __init__(self):
        self.driver = Driver().connect()

    def log_in(self):
        # first open div containing fields for logging in
        self.driver.find_element_by_id('btn-login').click()

        logserver_select = Select(self.driver.find_element_by_id(
            conf.logserver_field_id))
        username_input = self.driver.find_element_by_id(conf.username_field_id)
        password_input = self.driver.find_element_by_id(conf.password_field_id)
        submit_button = self.driver.find_element_by_id(conf.login_button_id)

        logserver_select.select_by_visible_text(credentials.server)
        username_input.send_keys(credentials.username)
        password_input.send_keys(credentials.password)

        submit_button.click()
        return self.wait_until_logged()

    def wait_until_logged(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     conf.logged_in_check_element))
            )
            return True
        except:
            print("[ERROR] Timeout occured while waiting for log in.")
            self.driver.save_screenshot('logging-in-err.png')
            return False
