from components.components import WebElement
from pages.base_page import BasePage


class CheckBox(BasePage):         # класс
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/checkbox"
        super().__init__(driver, self.base_url)

        self.checkbox1 = WebElement(driver, "span.rct-title")
        self.btn_plus = WebElement(driver, ".rct-option.rct-option-expand-all > svg > path")