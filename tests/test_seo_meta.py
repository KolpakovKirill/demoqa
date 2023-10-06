from pages.accordion import Accordion
from pages.alerts import Alert
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
import time
import pytest


@pytest.mark.parametrize("pages", [Accordion, Alert, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(4)
    assert page.head_viewport.exist()
    assert page.head_viewport.get_dom_attribute('name') == 'viewport'
    assert page.head_viewport.get_dom_attribute('content') =='width=device-width,initial-scale=1'

#не паботает