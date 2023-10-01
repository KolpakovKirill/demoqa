import time
from conftest import browser
from pages.koup import Koup
from pages.koup_add import KoupAdd


def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements' # соответствие текста
    koup_page.link_add.click()
    time.sleep(2)
    assert koup_add.equal_url()  # проверяет, что текущий URL страницы соответствует ожидаемому URL-адресу
    assert koup_add.btn_add.get_text() == "Add Element"
    assert koup_add.btn_add.get_dom_attribute("onclick") == "addElement()" # С помощью метода `get_dom_attribute` можно получить значение конкретного атрибута DOM элемента на веб-странице
    #? почему мы здесь выбрали oneclic? можно-ли было выбрать что-нибудь еще?
    time.sleep(2)
    for i in range(4):  # кликнуть на кнопку 4 раза
        koup_add.btn_add.click()
    time.sleep(2)
    assert koup_add.btns_delete.check_count_elements(4) # утверждение (assert), которое проверяет, что количество элементов, найденных с помощью метода `check_count_elements(4)` объекта `btns_delete`, равно 4

    for element in koup_add.btns_delete.find_elements():  # в цикле `for` проходится по всем элементам найденным с помощью метода `find_elements()` объекта `btns_delete` и проверяется, что текст каждого элемента равен "Delete"
        assert element.text == "Delete"
    # проверка только для первого элемента
    assert koup_add.btns_delete.get_text() == "Delete"  # полученный текст равен Delete

    while koup_add.btns_delete.exist():  # цикл `while`, который будет выполняться до тех пор, пока объект `btns_delete` существует (exist).  спомощью `click()` по локатору `btns_delete`.
        koup_add.btns_delete.click()
    assert not koup_add.btns_delete.exist()  # Затем, после окончания цикла, проверяется, что koup_add.btns_delete больше не существует .

