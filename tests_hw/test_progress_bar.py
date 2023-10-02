from pages.progress_bar import ProgressBar
import time


def test_progress_bar(browser):
    progress_bar_moving = ProgressBar(browser)
    progress_bar_moving.visit()
    time.sleep(2)
    progress_bar_moving.btn_start_stop.click()
    time.sleep(5.1)
    progress_bar_moving.btn_start_stop.click()
    assert progress_bar_moving.progress_bar.get_dom_attribute("aria-valuenow") == "51" # утверждение, которое проверяет, что текущее значение атрибута aria-valuenow прогресс-бара равно "51"
    time.sleep(4)
