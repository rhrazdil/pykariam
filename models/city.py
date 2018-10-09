from navmazing import NavigateStep, NavigateToSibling
from utils.ui import click, element_fill, element, element_text, is_element_present, elements
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

class Cities(object):
    def __init__(self):
        self.cities = {}
        self.city_names = self._get_city_names()

    # TODO this is a perfect candidate to wrap with some open&close wrapper
    @staticmethod
    def _get_city_names():
        click('js_citySelectContainer')
        cities = [city.text.split()[1] for city in
                  elements('//*[@id="dropDown_js_citySelectContainer"]/div[1]/ul/li')]
        # cities_dict = {k:v for k, v in enumerate(cities)}
        click('js_citySelectContainer')
        return cities


    @staticmethod
    def _get_buildings_map():
        buildings_map = dict()
        for position in range(0, 19):
            elem = element('js_CityPosition' + str(position) + 'Link')
            title = elem.get_attribute('title')
            name = title if '(' not in title else title.split('(')[0].rstrip()
            level = -1 if '(' not in title else title.split('(')[1].rstrip(')')
            building = Building(name, level, position)
            buildings_map.update({name: building})
        return buildings_map


    def scan_cities(self):
        for city_name in self.city_names:




class City(object):
    def __init__(self, name, buildings):
        self.name = name # element_text('#js_citySelectContainer > span > a', 'css').split()[1]
        self.buildings = buildings




@navigator.register(City, 'All')
class CityOverview(NavigateStep):
    def am_i_here(self, *args, **kwargs):
        raise NotImplementedError

    def step(self, *args, **kwargs):
        Login().ensure_logged()
        click('js_cityLink')


class Building(object):
    def __init__(self, name, level, position):
        self.name = name
        self.level = level
        self.position = position
