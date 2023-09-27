from conftest import browser
from pages.form_page import FromPage
import time
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    page = FromPage(browser)
    page.visit()
    browser.set_window_size(1500, 1500)
    page.first_name.send_keys('tester')
    time.sleep(2)
    page.last_name.send_keys('testerovich')
    time.sleep(2)
    page.user_email.send_keys('testerovich@ttt.tt')
    time.sleep(2)
    page.gender_radio_1.click_force()
    time.sleep(2)
    page.user_number.send_keys("1233333333")

def test_state_2(browser):     # переделать локаторы
    form_page1 = FromPage(browser)

    form_page1.visit()
    time.sleep(2)
    form_page1.state.scrol_to_element()
    time.sleep(2)
    form_page1.state2.send_keys("NCR")
    form_page1.state2.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_3 (browser):      # переделать локаторы
    from_page2 = FromPage(browser)

    from_page2.visit()
    time.sleep(2)
    from_page2.state.scroll_to_element()
    time.sleep(2)
    from_page2.state2.click()
    from_page2.state2.send_keys(Keys.PAGE_DOWN)
    from_page2.state2.send_keys(Keys.ENTER)
    time.sleep(2)