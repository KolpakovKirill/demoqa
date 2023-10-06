from conftest import browser
from pages.radio_button import RadioButton
from pages.demoqa import DemoQa
import pytest


@pytest.mark.skip    # предназначен для пропуска выполнения определенного теста
def test_decor(browser):
    demoqa_page = DemoQa(browser)

    demoqa_page.visit()
    assert demoqa_page.headers_h5.check_count_elements(6)  # Метод проверяет, что количество заголовков h5 равно 6.
    for element in demoqa_page.headers_h5.find_elements():  # происходит проверка, что каждый заголовок h5 не пустой
        assert not element.text == ""


# @pytest.mark.skipif(True, reason="Just Skip")
def test_radio(browser):
    radio_btn_page = RadioButton(browser)

    if not radio_btn_page.code_status() == 200:  # Если страница недоступна (код статуса ответа от сервера не равен 200), то тест пропускается
        pytest.skip(reason=f"Страница {radio_btn_page.base_url} недоступна")

    radio_btn_page.visit()
    assert 'disable' in radio_btn_page.btn_no.get_dom_attribute('class') # Проверка, что кнопка с классом 'disable' находится на странице
    radio_btn_page.btn_yes.click_force()
    assert radio_btn_page.you_have_selected_yes.get_text() == 'Yes' # Клик по кнопке с надписью 'Yes' и проверка, что отображается текст 'Yes
    radio_btn_page.btn_impressive.click_force()
    assert radio_btn_page.you_have_selected_impressive.get_text() == 'Impressive' # Клик по кнопке с надписью 'Impressive' и проверка, что отображается текст 'Impressive'

# Если какой-либо из утверждений (assert) не проходит, то тест не пройдет