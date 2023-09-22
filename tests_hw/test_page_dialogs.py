from conftest import browser
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()
    assert modal_elements.btn_sidebar_modal_dialogs.check_count_elements(5, int)
