import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.basic
def test_all_options_present(browser):
    page = DropdownPage(browser).open_page()
    options = page.get_all_options()
    assert "Please select an option" in options
    assert "Option 1" in options
    assert "Option 2" in options


@pytest.mark.basic
def test_select_first_option(browser):
    page = DropdownPage(browser).open_page()
    page.select_by_index(1)
    assert page.selected_text() == "Option 1"


@pytest.mark.basic
def test_select_second_option(browser):
    page = DropdownPage(browser).open_page()
    page.select_by_index(2)
    assert page.selected_text() == "Option 2"