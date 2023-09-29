from pages.webtables import Webtables
from conftest import browser
import time


def test_webtables_two(browser):
    webtables_loc = Webtables(browser)
    webtables_loc.visit()
    webtables_loc.rows.click()
    time.sleep(10)
    webtables_loc.select_rows_5.click()
    # time.sleep(10)
    assert not webtables_loc.btn_next.click()
    assert not webtables_loc.btn_previos.click()

    webtables_loc.btn_add.click()
    webtables_loc.first_name.send_keys('Tester')
    webtables_loc.last_name.send_keys('Testerovich')
    webtables_loc.email.send_keys('Testerovich@yandex.ru')
    webtables_loc.age.send_keys('26')
    webtables_loc.salary.send_keys('777')
    webtables_loc.department.send_keys('123qwerty')
    webtables_loc.btn_submit.click_force()

    webtables_loc.btn_add.click()
    webtables_loc.first_name.send_keys('Tester')
    webtables_loc.last_name.send_keys('Testerovich')
    webtables_loc.email.send_keys('Testerovich@yandex.ru')
    webtables_loc.age.send_keys('26')
    webtables_loc.salary.send_keys('777')
    webtables_loc.department.send_keys('123qwerty')
    webtables_loc.btn_submit.click_force()

    webtables_loc.btn_add.click()
    webtables_loc.first_name.send_keys('Tester')
    webtables_loc.last_name.send_keys('Testerovich')
    webtables_loc.email.send_keys('Testerovich@yandex.ru')
    webtables_loc.age.send_keys('26')
    webtables_loc.salary.send_keys('777')
    webtables_loc.department.send_keys('123qwerty')
    webtables_loc.btn_submit.click_force()

    time.sleep(5)

    webtables_loc.btn_next.click()
    time.sleep(10)
    assert webtables_loc.page_rows.get_dom_attribute('value') == '2'
    webtables_loc.btn_previos.click()
    assert webtables_loc.page_rows.get_dom_attribute('value') == '1'
    time.sleep(10)
