from pages.alerts import Allert
from conftest import browser
import time
from components.components import WebElement
def test_allert(browser):
    page_test_allert = Allert(browser)

    page_test_allert.visit()
    assert not page_test_allert.alert()
    page_test_allert.alert_button.click()
    time.sleep(2)
    assert page_test_allert.alert()
    page_test_allert.alert().accept()

    page_test_allert.visit()
    page_test_allert.alert_button.click()
    time.sleep(2)
    assert page_test_allert.alert().text == "You clicked a button"
    page_test_allert.alert().accept()
    assert  not page_test_allert.alert()


def test_confirm(browser):
    page_test_allert = Allert(browser)

    page_test_allert.visit()

    page_test_allert.alert_button.click()
    time.sleep(2)
    page_test_allert.alert().dismiss()
    assert page_test_allert.alert().text == "You selected Cancel"


def test_prompt(browser):
    page_test_allert = Allert(browser)

    page_test_allert.visit()
    page_test_allert.alert_button.click()
    time.sleep(2)

    page_test_allert.alert().send_keys("Tetser")
    page_test_allert.alert().accept()
    assert page_test_allert.prompt_result.get_text() == "You entered Tester"
    time.sleep(2)
