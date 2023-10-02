import time

from components.components import WebElement
from pages.base_page import BasePage


class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')

        self.pencil = WebElement(driver, '#edit-record-4 > svg')
        self.del_record = WebElement (driver, "#delete-record-4")
        self.No_rows_found = WebElement (driver, "div.rt-noData")
        self.del_record1 = WebElement(driver,"#delete-record-1 > svg > path")
        self.del_record2 = WebElement (driver,"#delete-record-2 > svg > path")
        self.del_record3 = WebElement (driver,"#delete-record-3 > svg > path")
        self.rows = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.select_rows_5 = WebElement(driver,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.page_rows = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        self.btn_next = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.btn_previos = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')

        self.table_record1 = WebElement(driver, 'div.rt-tr-group:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.no_rows_found = WebElement (driver, "div.rt-noData")
        self.delete_btns = WebElement(driver, '[title="Delete"]')

        self.rows_per_page = WebElement(driver, '[aria-label="rows per page"]')
        self.rows_per_page_5 = WebElement(driver, '[aria-label="rows per page"] > [value="5"]')
        self.pages_count = WebElement(driver, '[class="-totalPages"]')
        self.prev_button = WebElement(driver, '.-previous > button:nth-child(1)')
        self.next_button = WebElement(driver, '.-next > button:nth-child(1)')
        self.page_jump = WebElement(driver, 'span > div [aria-label="jump to page"]')

        self.column_first_name = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(1)')
        self.column_last_name = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(2)')
        self.column_age = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(3)')
        self.column_email = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(4)')
        self.column_salary = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(5)')
        self.column_department = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(6)')
