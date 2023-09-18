from pages.elements_page import Footer
from conftest import browser
from pages.demoqa import DemoQa
def test_check_footer_text(browser):

    footer_page = Footer(browser)
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    assert footer_page.text_footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


