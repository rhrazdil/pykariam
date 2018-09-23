"""
UI utility methods

"""
from utils.driver import Driver


def click(selection, sel_type='id'):
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

    selector(selection).click()