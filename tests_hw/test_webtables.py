from pages.webtables import Webtables
from conftest import browser
import time
from selenium.webdriver.common.keys import Keys

def test_webtables(browser):
    page_webtables = Webtables(browser)
    page_webtables.visit()

    assert not page_webtables.table_record1.get_text() == '' # Утверждение, что первая запись в таблице не пуста
    assert not page_webtables.no_rows_found.exist()  # Утверждение, что сообщение "No rows found" не существует.

    while page_webtables.delete_btns.exist():  # конструкция `while` используется для повторного выполнения действия клика по кнопкам удаления, пока кнопки все еще существуют на странице.
        page_webtables.delete_btns.click()

    assert page_webtables.no_rows_found.exist()


def test_np_bttns(browser):
    page_webtables_loc = Webtables(browser)

    type_list = ['Firstname', 'LastName', 'user@email.com', 27, 90, 'department']

    page_webtables_loc.visit()
    page_webtables_loc.rows_per_page.scroll_to_element()
    page_webtables_loc.rows_per_page.click()
    page_webtables_loc.rows_per_page.send_keys(Keys.UP)
    page_webtables_loc.rows_per_page.send_keys(Keys.RETURN)
    page_webtables_loc.btn_add.scroll_to_element()
    assert page_webtables_loc.next_button.get_dom_attribute('disabled')
    assert page_webtables_loc.prev_button.get_dom_attribute('disabled')
    counter = 0
    while page_webtables_loc.pages_count.get_text() == '1':
        counter += 1    #в цикле выполняется 8 итераций
        page_webtables_loc.btn_add.click()
        page_webtables_loc.first_name.send_keys(type_list[0])
        page_webtables_loc.last_name.send_keys(type_list[1])
        page_webtables_loc.email.send_keys(type_list[2])
        page_webtables_loc.age.send_keys(type_list[3])
        page_webtables_loc.salary.send_keys(type_list[4])
        page_webtables_loc.department.send_keys(type_list[5])
        page_webtables_loc.btn_submit.click()
        time.sleep(1)
    assert counter == 8 # Если количество итераций будет отличаться, то утверждение `assert counter == 8` не будет выполняться
    assert page_webtables_loc.pages_count.get_text() == '2' #  поле с количеством страниц имеет значение "2"
    assert not page_webtables_loc.next_button.get_dom_attribute('disabled') #проверка что кнопка "Next" не отключена
    assert page_webtables_loc.page_jump.get_dom_attribute('value') == "1" # после ввода у стр. значение "1"
    page_webtables_loc.next_button.click_force()
    time.sleep(5)
    assert page_webtables_loc.page_jump.get_dom_attribute('value') == "2" # послее кнопки next стр. знач. "2"
    page_webtables_loc.prev_button.click_force()
    assert page_webtables_loc.page_jump.get_dom_attribute('value') == "1"  # послее кнопки prev стр. знач. "1"
    time.sleep(10)

