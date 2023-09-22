from pages.elements_page import ElementsPage
from conftest import browser
from pages.demoqa import DemoQa

def test_page_elements(browser):
    element_page = ElementsPage(browser)
    demo_qa_page = DemoQa(browser)

    element_page.visit()
    assert element_page.text_elements.get_text() == "Elements"
    assert element_page.btn_sidebar_first.exist()
    assert element_page.btn_sidebar_first_textbox.exist()

    demo_qa_page.visit()
    assert demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.btn_elements.click()
    assert element_page.text_center.get_text() == 'Please select an item from left to start practice.'




