from pages.base_page import BasePage
from components.components import WebElement
class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.btn_sidebar_modal_dialogs = WebElement(driver, '.show > ul:nth-child(1) > li')
