from conftest import browser
from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    assert modal_elements.btn_sidebar_modal_dialogs.check_count_elements(5)


def test_navigation_modal(browser):
    navigation_page = ModalDialogs(browser)
    navigation_page_2 = DemoQa(browser)
    navigation_page.visit()
    browser.refresh()
    navigation_page.demoqa_tools_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert navigation_page_2.equal_url()
    assert navigation_page_2.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)