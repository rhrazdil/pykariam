"""
UI utility methods

"""
from utils.driver import Driver
import time
import random


def get_selector_method(sel_type):
    driver = Driver().connect()
    selector = None

    if sel_type == 'id':
        selector = driver.find_element_by_id
    elif sel_type == 'xpath':
        selector = driver.find_element_by_xpath
    elif sel_type == 'text':
        selector = driver.find_element_by_visible_text
    elif sel_type == 'css':
        selector = driver.find_element_by_css_selector
    return selector


def click(selection, sel_type='id'):
    time.sleep(random.randint(1,5))  # sleep between 1 - 5 sec to mimic human
    selector = get_selector_method(sel_type)
    selector(selection).click()


def element(selection, sel_type='id'):
    """
    Return single element that matches selection of given selection type

    Args:
        selection (str): selection string
        sel_type (str): id, css, xpath or text (value)

    Returns:
        WebElement
    """
    selector = get_selector_method(sel_type)
    return selector(selection)


def elements(xpath_selection):
    """
    Return list of elements that match xpath selection

    Args:
        selection (str): xpath selection string

    Returns:
        WebElement
    """
    driver = Driver().connect()
    return driver.find_elements_by_xpath(xpath_selection)


def element_text(selection, sel_type='id'):
    selector = get_selector_method(sel_type)
    element = selector(selection)
    return element.text


def element_fill(selection, content, sel_type='id'):
    selector = get_selector_method(sel_type)
    element = selector(selection)
    element.send_keys(content)


def main_box_header_title():
    return element_text('#js_mainBoxHeaderTitle', sel_type='css')