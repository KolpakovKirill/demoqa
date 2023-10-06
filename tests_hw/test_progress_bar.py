from pages.progress_bar import ProgressBar
import time


def test_progress_bar(browser):
    page = ProgressBar(browser)

    page.visit()
    #time.sleep(2)
    page.btn_start_stop.click()
    while True:
        if page.progress_bar.get_dom_attribute("aria-valuenow") == "51":
            page.btn_start_stop.click_force()
            break

    # time.sleep(2)