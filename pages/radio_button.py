from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        super().__init__(driver, self.base_url)

        self.btn_yes = WebElement(driver, "#yesRadio")
        self.btn_impressive = WebElement(driver, "#noRadio")
        self.btn_no = WebElement(driver, "#noRadio")
        self.you_have_selected_yes = WebElement(driver, ".text-success") # поле с текстом (одинаковое и можно оставить одну строчку
        self.you_have_selected_impressive = WebElement(driver, ".text-success") # поле с текстом (одинаковое и можно оставить одну строчку
