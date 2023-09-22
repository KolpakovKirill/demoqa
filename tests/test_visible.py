import time

from conftest import browser
from pages.elements_page import ElementsPage
def test_visible_btn_sidebar(browser):
    visible_btn = ElementsPage(browser)
    visible_btn.visit()
    #visible_btn.btn_sidebar_first_textbox.click()
    #time.sleep(3)
    #assert visible_btn.btn_sidebar_first_textbox.exist()
    assert visible_btn.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.btn_sidebar_first_checkbox.visible()
    element_page.btn_sidebar_first_checkbox.click()
    time.sleep(2)
    assert not element_page.btn_sidebar_first_checkbox.visible()



