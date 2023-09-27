from pages.webtables import Webtables
from conftest import browser
import time


def test_webtables(browser):
    page_webtables = Webtables(browser)
    page_webtables.visit()
    page_webtables.btn_add.click()
    page_webtables.first_name.send_keys('Tester')
    page_webtables.last_name.send_keys('Testerovich')
    page_webtables.email.send_keys('Testerovich@yandex.ru')
    page_webtables.age.send_keys('26')
    page_webtables.salary.send_keys('777')
    page_webtables.department.send_keys('123qwerty')
    page_webtables.btn_submit.click_force()
    # time.sleep(9)

    page_webtables.pencil.click()
    page_webtables.first_name.clear()
    page_webtables.first_name.send_keys('Qwerty')
    page_webtables.btn_submit.click_force()
    #time.sleep(9999999)
    page_webtables.del_record.click_force()
    #time.sleep(9999999)

