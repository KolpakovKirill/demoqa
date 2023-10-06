from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa
from conftest import browser


def test_go_topage_elements(browser):      #
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()


def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    # elements_page.icon.click()
    assert elements_page.icon.exist()



def test_check_sidebar_button(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    # elements_page.icon.click()
    assert elements_page.btn_sidebar_first.exist()


def test_check_sidebar_first_nested_button(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    # elements_page.icon.click()
    assert elements_page.btn_sidebar_first_textbox.exist()
