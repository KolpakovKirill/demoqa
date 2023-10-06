import time
from selenium.webdriver import Keys
from pages.slider import Slider



def test_slider(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.btn_slider.exist()
    assert slider.number_field.exist()

    while slider.number_field.get_dom_attribute('value') != '50':   # Затем, с помощью цикла, кнопка ползунка смещается вправо, пока значение числового поля не станет равным '50'. Это может быть сделано с помощью метода send_keys() объекта btn_slider, который, отправляет клавишу стрелки вправо.
        slider.btn_slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.number_field.get_dom_attribute('value') == '50'

# -----

# через drag_and_drop_by_offset  не правильно