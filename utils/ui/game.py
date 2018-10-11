from utils.ui import is_element_present, click


def close_popup():
    """
    Function tries to close any popup window that may or may not be displayed upon login

    Returns:
         None

    """
    if is_element_present('multiPopup'):
        click('//*[@id="multiPopup"]/div[2]/div[2]/a', sel_type='xpath')


def view_city():
    if not is_element_present('js_cityBread'):
        click('js_cityBread')