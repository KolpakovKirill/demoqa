from conftest import browser
from pages.form_page import FromPage
import time
def test_login_form(browser):
    form_page = FromPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testerovich")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("9992223344")
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

    form_page.hobbies.click_force()
    form_page.current_address.send_keys("address")

    #form_page.state.click_force()
    #time.sleep(2)
    form_page.state.find_element("stateCity-wrapper").find_element("input.select-dropdown")
    #form_page.state.send_keys("New York")
    time.sleep(2)
    form_page.state.find_element("stateCity-wrapper").find_element("ul.select-dropdown"))
    state_city_dropdown.select_by_visible_text("New York")
    #form_page.state3.click_force()

    #input.select - dropdown