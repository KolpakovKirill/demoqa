import time
from conftest import browser
from pages.text_box import TextBox

def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.full_name.send_keys('Test')
    time.sleep(3)
    text_box_page.current_address.send_keys('NewYork')
    time.sleep(3)
    text_box_page.btn_submit.click()
    time.sleep(3)

    assert text_box_page.usr_name_sent.get_text() == 'Name:Test'
    time.sleep(3)
    assert text_box_page.current_addr_sent.get_text() == "Current Address:NewYork"
    time.sleep(3)
