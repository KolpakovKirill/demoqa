from pages.elements_page import ElementsPage


from conftest import browser
def test_page_elements(browser):
    elements_pages = ElementsPage(browser)

    elements_pages.visit()
    assert elements_pages.text_elements.get_text() == "Elements"







