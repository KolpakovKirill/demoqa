import logging
from components.components import WebElement
#from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver            #
        self.base_url = base_url     #"https://demoqa.com/"
        self.head_viewport = WebElement(driver, "head>meta[name = 'viewport']")

    def visit(self):
        return self.driver.get(self.base_url)

    def get_url(self):                #метод должен возвращать текущий урл
        return self.driver.current_url

    def equal_url(self):              #метод должен вызывать get_url сравнивать его со строкой 'https://demoqa.com/'
        if self.get_url() == self.base_url:
            return True
        return False

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def alert(self):     # переключение на всплывающее окно (alert) веб-страницы
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

# Если возникла ошибка при переключении на всплывающее окно или его не удалось найти, то метод возвращает False