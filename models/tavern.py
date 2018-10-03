from navmazing import NavigateStep, NavigateToSibling
from utils.ui import click, element_text, element, elements, main_box_header_title
from utils.navigator import Navigator

navigator = Navigator().navigator()


class Tavern(object):
    def __init__(self):
        self.name = 'Tavern'
        self.id = 'js_CityPosition7Link'  # TODO: figure building positions automagically

    def set_max_consumption(self):
        navigator.navigate(self, 'All')

        # open dropdown menu
        click(
            '#js_wineAmountContainer > span',
            'css'
        )

        # select last item
        elements(
            "//*[@id='dropDown_js_wineAmountContainer']/div[1]/ul/li",
        )[-1].click()

        # submit changes
        click(
            '#wineAssignForm > div.content_right > div.centerButton > input',
            'css'
        )


@navigator.register(Tavern, 'All')
class TavernOverview(NavigateStep):
    def am_i_here(self):
        return False

    def step(self):
        click('js_cityLink')
        click(self.obj.id)
