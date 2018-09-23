from navmazing import NavigateStep, NavigateToSibling
from utils.ui import click, element_text, element_fill, main_box_header_title
from utils.navigator import Navigator

navigator = Navigator().navigator()


class PirateFortress(object):
    def __init__(self):
        self.name = 'Pirate Fortress'
        self.id = 'js_CityPosition17Link'  # TODO: figure building positions automagically

    def launch_raid(self):
        navigator.navigate(self, 'Raid')
        click('//*[@id="pirateCaptureBox"]/div[1]/table/tbody/tr[1]/td[5]/a',
              sel_type='xpath')

    def add_crew_strength(self, amount):
        navigator.navigate(self, 'CrewStrength')
        element_fill(selection='CPToCrewInput', content=amount)
        click('CPToCrewSubmit')


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
        return False

    def step(self):
        click('js_cityLink')
        click(self.obj.id)
