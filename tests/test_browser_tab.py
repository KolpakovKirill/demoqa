from pages.browser_tab import BrowserTab
from conftest import browser
import time

def test_browser_tab(browser):
    browser_tab = BrowserTab(browser)

    browser_tab.visit()
                                   # открывает первую вкладку в браузере
    assert len(browser.window_handles) == 1    # Это проверка утверждает, что количество  окон браузер равно 1
    browser_tab.new_tab.click() # открывает новую вкладку в браузере
    #time.sleep(2)
    assert len(browser.window_handles) == 2  # Это проверка утверждает, что количество  окон браузер равно 2

    browser.switch_to.window(browser.window_handles[0])  # переключаемся обратно на первую вкладку.
    time.sleep(2)

# В целом, этот код проверяет корректность открытия новой вкладки в браузере.
