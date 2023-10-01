from pages.alerts import Alert
from conftest import browser
import time


def test_alert(browser):
    page_alert = Alert(browser)
    page_alert.visit()

    assert not page_alert.alert()
    page_alert.alert_button.click()
    time.sleep(2)
    assert page_alert.alert()
    page_alert.alert().accept()

def test_alert_text(browser):
    page_alert = Alert(browser)
    page_alert.visit()

    page_alert.alert_button.click()
    time.sleep(2)
    assert page_alert.alert().text == "You clicked a button"
    page_alert.alert().accept()
    assert  not page_alert.alert()


def test_confirm(browser):
    page_alert = Alert(browser)
    page_alert.visit()
    page_alert.confirm_button.click()
    time.sleep(2)
    page_alert.alert().dismiss()
    assert page_alert.confirm_result.get_text() == "You selected Cancel"


def test_prompt(browser):
    page_alert = Alert(browser)
    page_alert.visit()
    page_alert.alert_button.click()
    time.sleep(2)
    page_alert.alert().send_keys("Tester")
    page_alert.alert().accept()
    assert page_alert.prompt_result.get_text() == "You entered Tester"
    time.sleep(2)
