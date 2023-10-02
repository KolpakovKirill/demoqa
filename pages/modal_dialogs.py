from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.btn_sidebar_modal_dialogs = WebElement(driver, '.show > ul:nth-child(1) > li') #  не уникальный один из 5 под Alerts, Frame & Windows 5 кнопок в подсписке
        self.demoqa_tools_icon = WebElement(driver, '#app > header > a') # Заголовок

        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.modal_dialog_window = WebElement(driver, 'div.fade.modal.show') # Модальное окно отличается от алерта в этом примере подходит под обе кнопки Small и Large. Полный локатор   body > div.fade.modal.show > div > div > div.modal-body
        self.small_close = WebElement(driver, '#closeSmallModal')
        self.large_close = WebElement(driver, '#closeLargeModal')
        self.not_have = WebElement(driver, '#main-message > h1 > span')