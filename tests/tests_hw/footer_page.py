from components.components import WebElement
from pages.base_page import BasePage
class Footer(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)

        self.text_footer = WebElement(driver, "#app > footer")