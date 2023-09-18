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
