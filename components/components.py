from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=""):  #
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def exist(self):                    # Наличие элемента на веб-странице,если элемент не найден, метод вернет значение False
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):     #возвращает текст элемента веб-страницы, найденного с помощью метода find_element
        return str(self.find_element().text)


    def visible(self):
        return self.find_element().is_displayed()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count, int):
        self.count = count   #Поиск элементов на странице и проверка количества найденных элементов =  значению count
        self.int = int
        if len(self.find_elements()) == count:
            return True
        return False


#Или
#def check_count_elements(self, count: int):
        #return len(self.find_elements()) == count