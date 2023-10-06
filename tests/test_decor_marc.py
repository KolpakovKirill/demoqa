import pytest


@pytest.mark.smoke    # это тесты для быстрой проверки базового функционала программы
def test_decor_mark_1():
    assert True


@pytest.mark.regress  # что это тесты для проверки исправления ошибок и регрессий
def test_decor_mark_2():
    assert True


@pytest.mark.regress
def test_decor_mark_3():
    assert True


@pytest.mark.regress
def test_decor_mark_4():
    assert True
