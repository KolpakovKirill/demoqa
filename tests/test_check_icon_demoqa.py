from pages.demoqa import DemoQa
from conftest import browser
#from selenium.webdriver.common.by import By
from conftest import browser
from pages.demoqa import DemoQa

def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)  #
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.icon.exist()   #проверяем наличие иконки
    assert demo_qa_page.equal_url()

#def test_icon_exist(browser):

    # browser.get("https://demoqa.com/")
    # icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
    # if icon is None:
    #     print("Элемент не найден")
    # else:
    #     print("Элемент найден")


