from pages.base_page import BasePage
from components.components import WebElement
class Allert(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/alerts"
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'

        }

        self.alert_button = WebElement(driver, "#alertButton")
        self.confirm_button = WebElement (driver, "#confirmButt")
        self.confirm_result = WebElement (driver, "#confirmResult")
        self.promt_button = WebElement (driver, "#promtButton")
        self.prompt_result = WebElement (driver, "#promptResult")
        self.time_alert_button = WebElement(driver, '#timerAlertButton')