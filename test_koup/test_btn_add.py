from selenium.webdriver.common.keys import Keys
import time
from conftest import browser
from pages.koup import Koup
from pages.koup_add import KoupAdd
def test_herokuapp (browser):
    koup = Koup(browser)
    koup_page = KoupAdd(browser)
    koup.visit()

    assert koup.Link_add.get_text() == 'Add/Remove Elements'
    koup.Link_add.click()
    assert koup_page.equal_url()

    assert koup_page.btn_add.get_text() == "Add Element"

    assert koup_page.btn_add.get_dom_attribute("onclick") == "addElement()"
    # кликнуть на кнопку 4 раза
    for i in range(4):
        koup_page.btn_add.click()

    assert koup_page.btns_delete.check_count_elements(4)
    # проверка для всех элементов
    for element in koup_page.btns_delete.find_element():
        assert element.tetx == "Delete"
    # проверка только для первого элемента
    assert koup_page.btns_delete.get_text() == "Delete"
    while koup_page.btns_delete.exist():
        koup_page.btns_delete.click()
    assert not koup_page.btns_delete.exist()
