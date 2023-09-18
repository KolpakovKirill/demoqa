from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):         # класс
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6")
        self.text_elements = WebElement(driver, "#app > div > div > div.pattern-backgound.playgound-header > div")
        self.icon = WebElement(driver, "#app > header > a")
        self.btn_sidebar_first = WebElement(driver, "div:nth-child(1) > span > div")
        self.btn_sidebar_first_textbox = WebElement(driver, "div:nth-child(1) > div > ul > #item-0 > span")
        self.text_center = WebElement(driver, "div.col-12.mt-4.col-md-6")
    #def equal_url(self): #Убрали

#class Footer(BasePage):
    #def __init__(self, driver):
        #self.base_url = "https://demoqa.com/"
        #super().__init__(driver, self.base_url)
        #self.text_footer = WebElement(driver, "#app > footer")

