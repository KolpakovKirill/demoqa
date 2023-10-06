import time
from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_size(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


def test_visible_nav_bar(browser):
    visible_nav = ElementsPage(browser)
    visible_nav.visit()
    assert not visible_nav.btn_sidebar_nav.visible()

    browser.set_window_size(767, 1000)
    assert visible_nav.btn_sidebar_nav.visible()
    browser.set_window_size(1000, 1000)
