import pytest
from pages.add_remove_page import AddRemovePage


@pytest.mark.basic
def test_initial_state_has_no_delete_buttons(browser):
    page = AddRemovePage(browser).open_page()
    assert len(page.delete_buttons()) == 0


@pytest.mark.basic
def test_add_one_element_creates_one_delete_button(browser):
    page = AddRemovePage(browser).open_page()
    page.click_add()
    page.wait_delete_count(1)
    assert len(page.delete_buttons()) == 1


@pytest.mark.basic
def test_add_two_elements_creates_two_delete_buttons(browser):
    page = AddRemovePage(browser).open_page()
    page.click_add()
    page.wait_delete_count(1)
    page.click_add()
    page.wait_delete_count(2)
    assert len(page.delete_buttons()) == 2


@pytest.mark.basic
def test_delete_removes_one_element(browser):
    page = AddRemovePage(browser).open_page()
    page.click_add()
    page.wait_delete_count(1)
    page.click_add()
    page.wait_delete_count(2)
    page.click_delete()
    page.wait_delete_count(1)
    assert len(page.delete_buttons()) == 1