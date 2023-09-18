from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):         # класс
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, "#app > div > div > div.pattern-backgound.playgound-header > div")
        self.text_elements = WebElement(driver, "div.playgound-header > div")

class Footer(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)

        self.text_footer = WebElement(driver, "#app > footer")