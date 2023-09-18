
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebElement:
    def __init__(self, driver, locator=""):  #
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):                # перенесли из base_page
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):                    #существование элемента, добавили из Demoqa
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):              #возвращает какой текст кнопки которую находит
        return str(self.find_element().text)


    def visible(self):
        return self.find_element().is_displayed()
