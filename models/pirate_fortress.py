from navmazing import NavigateStep, NavigateToSibling
from utils.ui import click
from utils.navigator import Navigator

navigator = Navigator().navigator()


class PirateFortress(object):
    def __init__(self):
        self.name = 'test'
        self.id = 'js_CityPosition17Link'

    def raid(self):
        click('//*[@id="pirateCaptureBox"]/div[1]/table/tbody/tr[1]/td[5]/a',
              sel_type='xpath')

    def crew

    def farm_raids(self):



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
class PirateFortressOveriew(NavigateStep):
    def am_i_here(self):
        return False

    def step(self):
        click('js_cityLink')
        click(self.obj.id)
