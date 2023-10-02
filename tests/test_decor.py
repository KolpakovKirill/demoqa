from conftest import browser
from pages.radio_button import RadioButton
from pages.demoqa import DemoQa
import pytest


#@pytest.mark.skipif(True, reason="просто пропуск")
def test_decor1(browser):
    radio = DemoQa(browser)

    if not radio.code_status():
        pytest.skip(reason=f"Страница {radio.base_url} недоступна")

    radio.visit()
    radio.btn_yes.click_force()
    assert radio.headers_h5.check_count_elements(6)

    for element in radio.headers_h5.find_elements():
        assert element.text != ""


def test_decor2(browser):
    page_radio = RadioButton(browser)

    page_radio.visit()
    page_radio.btn_yes.click_force()
    assert page_radio.you_have_selected_yes.get_text() == "You have selected Yes"

    page_radio.btn_impressive.click_force()
    assert page_radio.you_have_selected_impressive.get_text() == "You have selected Impressive"


    assert "disabled" in page_radio.btn_no.get_dom_attribute("class")



