from navmazing import NavigateStep, NavigateToSibling
from utils.ui import (click, element_fill, element, element_text,
                      is_element_present, elements, city_dropdown)
from utils.navigator import Navigator
from utils.strings import Strings
from selenium.common.exceptions import NoSuchElementException
from conf import language
from utils.login import Login
from models import Building
from functools import wraps
import logging.config


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('PYKARIAM')

navigator = Navigator().navigator()
strings = Strings(language)


class Cities(object):
    def __init__(self):
        self.cities = {}
        self.city_names = {k:v for k, v in list(enumerate(self.get_city_names()))}

    @staticmethod
    @city_dropdown
    def get_city_names():
        cities = [city.text for city in elements('//*[@id="dropDown_js_citySelectContainer"]/div[1]/ul/li')]
        return cities

    @staticmethod
    def _current_city_map():
        buildings_map = dict()
        for position in range(0, 19):
            elem = element('js_CityPosition' + str(position) + 'Link')
            title = elem.get_attribute('title')
            name = title if '(' not in title else title.split('(')[0].rstrip()
            level = -1 if '(' not in title else title.split('(')[1].rstrip(')')
            building = Building(name, level, position)
            buildings_map.update({name: building})
        return buildings_map

    def _scan_city(self, city_name, city_index):
        city = City(city_name, city_index)
        navigator.navigate(city, 'All')
        return self._current_city_map()

    def scan_cities(self):
        for city_index, city_name in self.city_names.items():
            self.cities.update(
                {city_name: self._scan_city(city_name, city_index)}
            )


class City(object):
    def __init__(self, name, index, buildings=None):
        self.name = name  # element_text('#js_citySelectContainer > span > a', 'css').split()[1]
        self.index = index
        self.buildings = buildings

    def get_city_link_from_dropdown(self):
        element('js_citySelectContainer').click()
        city_links = elements('//*[@id="dropDown_js_citySelectContainer"]/div[1]/ul/li/a')
        for city_link in city_links:
            if city_link.text == self.name:
                return city_link


@navigator.register(City, 'All')
class CityOverview(NavigateStep):
    def am_i_here(self, *args, **kwargs):
        if element_text('js_cityBread') == self.obj.name:
            return True
        else:
            return False

    def step(self, *args, **kwargs):
        Login().ensure_logged()
        click('js_cityLink')

        element('js_citySelectContainer').click()

        click('//*[@id="dropDown_js_citySelectContainer"]/div[1]/ul/li[{}]/a'.format(str(self.obj.index + 1)), 'xpath')

        element('js_citySelectContainer').click()

