import pytest
from selenium.webdriver.common.keys import Keys
from pages.inputs_page import InputsPage


@pytest.mark.basic
def test_numeric_input_is_accepted(browser):
    page = InputsPage(browser).open_page()
    page.type_text("42")
    assert page.value() == "42"


@pytest.mark.advanced
def test_non_numeric_input_is_ignored(browser):
    page = InputsPage(browser).open_page()
    page.type_text("abc")
    # Поле числовое — буквы не принимаются.
    assert page.value() == ""


@pytest.mark.advanced
def test_arrow_up_increases_value(browser):
    page = InputsPage(browser).open_page()
    page.press_key(Keys.ARROW_UP)
    assert page.value() == "1"
    page.press_key(Keys.ARROW_UP)
    assert page.value() == "2"


@pytest.mark.advanced
def test_arrow_down_decreases_value(browser):
    page = InputsPage(browser).open_page()
    page.press_key(Keys.ARROW_UP)
    page.press_key(Keys.ARROW_UP)   # value == 2
    page.press_key(Keys.ARROW_DOWN)
    assert page.value() == "1"
    page.press_key(Keys.ARROW_DOWN)
    assert page.value() == "0"