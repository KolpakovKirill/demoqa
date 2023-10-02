from pages.base_page import BasePage
from components.components import WebElement


class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'

        super().__init__(driver, self.base_url)

        self.btn_slider = WebElement(driver, '#sliderContainer > div.col-9 > span > input') # Ползунок
        self.number_field = WebElement(driver, '#sliderValue') # меняющиеся цифры от ползунка с левой стороны