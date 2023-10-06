from conftest import browser
from pages.checkbox import CheckBox
from pages.elements_page import ElementsPage


def test_find_elements(browser):
    test_count_elements_page = ElementsPage(browser)
    test_count_elements_page.visit()
    assert test_count_elements_page.btn_fist_menu.check_count_elements(9)


def test_count_checkbox(browser):
    count_checkbox = CheckBox(browser)
    count_checkbox.visit()
    assert count_checkbox.checkbox1.check_count_elements(1)
    count_checkbox.btn_plus.click()
    assert count_checkbox.checkbox1.check_count_elements(17)
    count_checkbox.refresh()     #
    assert count_checkbox.checkbox1.check_count_elements(1)

