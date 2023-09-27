from conftest import browser
from pages.elements_page import ElementsPage
import time
def test_flex_menu(browser):
    flex_page = ElementsPage(browser)
    flex_page.visit()
    flex_page.block_menu.check_css("flex", "0 0 25%")
    flex_page.block_menu.check_css("flex", "0 0 100%")

    browser.set_window_size(650, 1000)
    flex_page.block_menu.check_css("max-width", "0 0 100%" )
    flex_page.block_menu.check_css("flex", "0 0 100%")
    browser.set_window_size(1000, 1000)
