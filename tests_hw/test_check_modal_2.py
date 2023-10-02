import time
from pages.modal_dialogs import ModalDialogs
import pytest
import requests




def test_page_availabil(browser):
    modal_d_btn = ModalDialogs(browser)
    modal_d_btn.visit()
    if modal_d_btn.code_status == 200:
        pytest.skip("Страница недоступна")

def test_page_availability():
    url = "https://demoqa.com/modal-dialogs"
    response = requests.get(url)
    if response.status_code != 200:
        pytest.skip("Страница недоступна")