from conftest import browser
from pages.accordion import Accordion
import time
def test_visible_accordion(browser):
    visible_accordion = Accordion(browser)
    visible_accordion.visit()
    assert visible_accordion.accordian_content_text.visible()
    visible_accordion.heading_text.click()
    time.sleep(2)
    assert not visible_accordion.accordian_content_text.visible()


def test_visible_accordion_default(browser):
    visible_accordion = Accordion(browser)
    visible_accordion.visit()
    #assert visible_accordion.accordian_text1_content2.visible()
    #assert visible_accordion.accordian_text2_content2.visible()
    #assert visible_accordion.accordian_text1_content3.visible()
    assert not visible_accordion.accordian_text1_content2.visible()
    assert not visible_accordion.accordian_text2_content2.visible()
    assert not visible_accordion.accordian_text1_content3.visible()
