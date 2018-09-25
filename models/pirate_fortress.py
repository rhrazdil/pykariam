from navmazing import NavigateStep, NavigateToSibling
from utils.ui import click, element_fill, element, element_text, is_element_present
from utils.navigator import Navigator
from utils.captcha import Captcha
from utils.strings import Strings
from selenium.common.exceptions import NoSuchElementException


navigator = Navigator().navigator()
strings = Strings('czech')


class PirateFortress(object):
    def __init__(self):
        self.name = strings['pirate_fortress']
        self.id = 'js_CityPosition17Link'  # TODO: figure building positions automagically
        self.captcha_filename = 'captcha.png'
        self.captcha_attempts = 3

    def raid(self):
        navigator.navigate(self, 'Raid')

        try:
            click('//*[@id="pirateCaptureBox"]/div[1]/table/tbody/tr[1]/td[5]/a',
                  sel_type='xpath')
        except NoSuchElementException as e:
            if self.is_captcha_displayed():
                pass
            else:
                raise
        except Exception as e:
            print("ERROR:", e)

        attempts = self.captcha_attempts
        while self.is_captcha_displayed() and attempts > 0:
            try:
                self.submit_captcha()
            except Exception as e:
                print(e)
            attempts -= 1

    def add_crew_strength(self, amount):
        navigator.navigate(self, 'CrewStrength')
        element_fill(selection='CPToCrewInput', content=amount)
        click('CPToCrewSubmit')

    @staticmethod
    def is_captcha_displayed():
        return is_element_present('captcha')

    @staticmethod
    def get_captcha_png():
        captcha = element('//*[@id="pirateCaptureBox"]/div[1]/form/img[@src]',
                          'xpath')
        return captcha.screenshot_as_png

    def save_image_to_file(self, image):
        with open(self.captcha_filename, 'wb') as file:
            file.write(image)

    def submit_captcha(self):
        # Save captcha image
        self.save_image_to_file(self.get_captcha_png())

        # First find solution from image
        captcha_solver = Captcha(self.captcha_filename)
        solution = captcha_solver.solve()

        # Fill captcha text field with found solution
        captcha_field = element('captcha')
        captcha_field.send_keys(solution)

        # Submit solution
        element(
            '#pirateCaptureBox > div.content > form > div.centerButton > input',
            'css'
        ).click()


@navigator.register(PirateFortress, 'Raid')
class PirateFortressRaid(NavigateStep):
    prerequisite = NavigateToSibling('All')

    def step(self):
        click('js_tabBootyQuest')


@navigator.register(PirateFortress, 'CrewStrength')
class PirateFortressCrewStrength(NavigateStep):
    prerequisite = NavigateToSibling('All')

    def step(self):
        click('js_tabCrew')


@navigator.register(PirateFortress, 'All')
class PirateFortressOverview(NavigateStep):
    def am_i_here(self):
        title_id = 'js_mainBoxHeaderTitle'
        if is_element_present(title_id) and element_text(title_id) == self.obj.name:
            return True
        else:
            return False

    def step(self):
        click('js_cityLink')
        click(self.obj.id)
