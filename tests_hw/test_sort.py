from pages.webtables import Webtables


def test_sort_by(browser):
    sort = Webtables(browser)
    sort.visit()
    assert sort.column_first_name.get_dom_attribute('class') == sort.column_last_name.get_dom_attribute(
        'class') == sort.column_age.get_dom_attribute('class') == sort.column_email.get_dom_attribute(
        'class') == sort.column_salary.get_dom_attribute('class') == sort.column_department.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -cursor-pointer'
    sort.column_first_name.click()
    assert sort.column_first_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort.column_last_name.click()
    assert sort.column_last_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort.column_age.click()
    assert sort.column_age.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort.column_salary.click()
    assert sort.column_salary.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort.column_email.click()
    assert sort.column_email.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort.column_department.click()
    assert sort.column_department.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
