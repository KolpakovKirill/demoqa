from tests.tests_hw.footer_page import Footer
from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_footer_text(browser):
    footer_page = DemoQa(browser)

    footer_page.visit()
    assert footer_page.footer_text.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


def test_check_text_center(browser):

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    elements_page = ElementsPage(browser)

    assert elements_page.text_center.get_text() == "Please select an item from left to start practice."





#def test_check_footer_text(browser):

    #footer_page = Footer(browser)
    #footer_page.visit()

    #assert footer_page.text_footer.exist()
    #assert footer_page.text_footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    #assert footer_page.text_footer.get_footer_text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
