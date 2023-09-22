from conftest import browser
from pages.elements_page import ElementsPage

def test_find_elements(browser):
    test_count_elements_page = ElementsPage(browser)
    test_count_elements_page.visit()
    assert test_count_elements_page.btn_fist_menu.check_count_elements(9, int)