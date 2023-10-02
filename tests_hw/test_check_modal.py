import time
from pages.modal_dialogs import ModalDialogs
import pytest
import requests


#@pytest.mark.skipif(not is_page_accessible(HomePage.URL), reason='Страница недоступна')
@pytest.mark.xfail(condition=True, reason="Если страница недоступна, то тест пропускается")
def test_small_large_modal(browser):
    modal_d_btn = ModalDialogs(browser)
    modal_d_btn.visit()

    assert modal_d_btn.small_modal.exist()
    assert modal_d_btn.large_modal.exist()
    modal_d_btn.small_modal.click()
    assert modal_d_btn.modal_dialog_window.exist()
    modal_d_btn.small_close.click()
    assert not modal_d_btn.modal_dialog_window.exist()
    modal_d_btn.large_modal.click()
    assert modal_d_btn.modal_dialog_window.exist()
    modal_d_btn.large_close.click()
    assert not modal_d_btn.modal_dialog_window.exist()


