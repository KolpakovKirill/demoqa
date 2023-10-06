from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.base_page import BasePage


def test_navigation(browser):
    demo_qa_page_1 = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page_1.visit()
    elements_page.btn_sidebar_first.click()

    browser.refresh()
    browser.back()
    browser.forward()
    elements_page.equal_url()
