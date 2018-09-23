from navmazing import Navigate, NavigateStep, NavigateToSibling
from utils.ui import click

navigator = Navigate()


class PirateFortress(object):
    def __init__(self):
        self.id = 'js_CityPosition17Link'


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


@navigator.register(PirateFortress, 'Overview')
class PirateFortressOveriew(NavigateStep):
    def am_i_here(self):
        return False

    def step(self):
        click('js_cityLink')
        click(self.obj.id)
