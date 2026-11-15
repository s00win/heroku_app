import pytest
from pages.checkboxes_page import CheckboxesPage


@pytest.mark.basic
def test_first_checkbox_initially_unchecked(browser):
    page = CheckboxesPage(browser).open_page()
    assert page.is_checked(0) is False


@pytest.mark.basic
def test_first_checkbox_can_be_checked(browser):
    page = CheckboxesPage(browser).open_page()
    page.toggle(0)
    assert page.is_checked(0) is True


@pytest.mark.basic
def test_second_checkbox_initially_checked(browser):
    page = CheckboxesPage(browser).open_page()
    assert page.is_checked(1) is True


@pytest.mark.basic
def test_second_checkbox_can_be_unchecked(browser):
    page = CheckboxesPage(browser).open_page()
    page.toggle(1)
    assert page.is_checked(1) is False