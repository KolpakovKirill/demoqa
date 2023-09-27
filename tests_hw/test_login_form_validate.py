import time

from pages.form_page import FromPage

from conftest import browser
def test_login_form (browser):
    login_form = FromPage(browser)
    login_form.visit()
    assert login_form.first_name.get_dom_attribute("placeholder") == "First Name"
    assert login_form.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert login_form.user_email.get_dom_attribute("placeholder") == "name@example.com"
    assert login_form.user_email.get_dom_attribute("pattern") == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"

    login_form.btn_submit.click_force()
    time.sleep(2)
    #assert login_form.use_form.get_dom_attribute("was-validated'") == "<class>"
    #assert login_form.use_form.get_dom_attribute("was-validated'") == "<form>"