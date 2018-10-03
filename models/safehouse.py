from navmazing import NavigateStep, NavigateToSibling
from utils.ui import click, element_fill, element, element_text, is_element_present
from utils.navigator import Navigator
from utils.strings import Strings
from selenium.common.exceptions import NoSuchElementException
from conf import language
from utils.login import Login
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('PYKARIAM')

navigator = Navigator().navigator()
strings = Strings(language)


class Safehouse(object):
    def __init__(self):
        self.name = strings['safehouse']
        self.id = 'js_CityPosition12Link'  # TODO: figure building positions automagically

    def train_spies(self):
        raise NotImplementedError

    def retreat_spies(self):
        raise NotImplementedError


@navigator.register(Safehouse, 'All')
class SafehouseOverview(NavigateStep):
    def am_i_here(self, *args, **kwargs):
        return False

    def step(self, *args, **kwargs):
        Login().ensure_logged()
        click('js_cityLink')
        click(self.obj.id)
