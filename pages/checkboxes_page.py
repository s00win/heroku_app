from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    PATH = "/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "[type='checkbox']")

    def open_page(self):
        return self.open(self.PATH)

    def get_checkboxes(self) -> list:
        return self.wait_presence_all(self.CHECKBOXES)

    def is_checked(self, index: int) -> bool:
        return self.get_checkboxes()[index].is_selected()

    def toggle(self, index: int):
        self.get_checkboxes()[index].click()
        return self