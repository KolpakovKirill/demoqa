from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

        self.accordian_content_text = WebElement(driver, "#section1Content")
        self.heading_text = WebElement(driver, "#section1Heading")
        self.accordian_text1_content2 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.accordian_text2_content2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.accordian_text1_content3 = WebElement(driver, "#section3Content > p")
