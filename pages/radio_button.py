from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        super().__init__(driver, self.base_url)

        self.btn_yes = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(2) > label")
        self.btn_impressive = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3) > label")
        self.btn_no = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div.custom-control.disabled.custom-radio.custom-control-inline > label")
        self.you_have_selected_yes = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p")
        self.you_have_selected_impressive = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p")
