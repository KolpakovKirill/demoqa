from conftest import browser
import time
from pages.alerts import Allert


def test_time_allert(browser):
    page_alert = Allert(browser)
    page_alert.visit()

    assert not page_alert.alert()
    page_alert.time_alert_button.click()
    time.sleep(7)
    assert page_alert.alert()
    page_alert.alert().accept()
