from pages.form_page import FromPage

from conftest import browser
def test_login_form (browser):
    login_form = FromPage(browser)
    login_form.visit()
