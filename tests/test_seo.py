import time

import pytest

from conftest import browser
from pages.accordion import Accordion
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa



def test_seo(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize("pages", [Accordion, Alert, DemoQa, BrowserTab ])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    # time.sleep(2)
    assert page.get_title() == 'DEMOQA'