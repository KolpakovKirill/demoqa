from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchDriverException, NoSuchElementException


def visit(self):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.home-body > div > div:nth-child")
        print("Элемент Лого найден")
    except NoSuchElementException:
        print("Элемент Лого не найден")


def get_url(self):
    return self.driver.current_url
