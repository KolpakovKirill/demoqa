from pages.alerts import Alert
from conftest import browser
import time


def test_alert(browser):  # Проверка алерта и подтверждение
    page_alert = Alert(browser)
    page_alert.visit()

    assert not page_alert.alert()  # алерт неактивен на странице
    page_alert.alert_button.click()
    time.sleep(1)
    assert page_alert.alert()  # алерт активен на странице
    page_alert.alert().accept()  # Принятие подтверждения

 # переключение на всплывающее окно веб-страницы - alert (), для принятия (подтверждения) алерта на веб-странице используется метод из класса "Alert" в библиотеке Selenium WebDriver - accept()


def test_alert_text(browser):
    page_alert = Alert(browser)
    page_alert.visit()

    page_alert.alert_button.click()
    time.sleep(2)
    assert page_alert.alert().text == "You clicked a button"  #  текст в активном алерте соответствует ожидаемому значению ("You clicked a button").
    page_alert.alert().accept()
    assert not page_alert.alert()   # проверяет, что активного алерта больше нет


def test_confirm(browser):  # Отмена алерта
    page_alert = Alert(browser)
    page_alert.visit()
    page_alert.confirm_button.click()
    time.sleep(2)
    page_alert.alert().dismiss() # Вызывается метод `dismiss()` в диалоговом окне alert, чтобы отменить его
    assert page_alert.confirm_result.get_text() == "You selected Cancel"  # Проверяется, что текст врезультате выбора кнопки Отмена - равен строке "You selected Cancel"



def test_prompt(browser):  # Вводим имя
    page_alert = Alert(browser)
    page_alert.visit()
    page_alert.prompt_button.click()
    time.sleep(2)
    page_alert.alert().send_keys("Tester") # вводим текст "Tester" в поле алерта с помощью метода `send_keys`
    page_alert.alert().accept()  # нажимаем кнопку "ОК"
    time.sleep(1)
    assert page_alert.prompt_result.get_text() == "You entered Tester"  # Проверка что после ввода есть текст "You entered Tester".
    time.sleep(2)
