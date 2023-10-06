from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class WebElement:
    def __init__(self, driver, locator="", locator_type="css"):  #
        self.driver = driver   # объект, представляющий веб-драйвер
        self.locator = locator   # описание местоположения элемента на странице).
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def exist(self):    # Cуществует ли элемент на странице
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True


    def get_text(self):     # возвращает текст элемента на странице в виде строки
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def check_count_elements(self, count: int): # позволяет проверять количество найденных элементов на странице, проверяет, что количество найденных элементов на странице соответствует заданному числу.
        self.count = count
        if len(self.find_elements()) == count:
            return True
        return False


    def send_keys(self, text: str):    # Позволяет вводить текст в поле элемента на странице
        self.find_element().send_keys(text)

    def click_force(self):     # нажмет на кнопку даже если ее невидно на странице (используеся JavaScript)
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + "a")
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):  # Позволяет получить значение атрибута DOM элемента. Если атрибут существует и имеет непустое значение, метод возвращает это значение.
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + "not correct")
        return False

    def scroll_to_element(self):   # прокрутка страницы до определенного элемента
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
            self.find_element()
        )

    def check_css(self, style, value=""):   # цвет фона, шрифт, размер или позиционирование.
        return self.find_element().value_of_css_property(style) == value


