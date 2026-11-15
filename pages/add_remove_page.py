from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddRemovePage(BasePage):
    PATH = "/add_remove_elements/"
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    def open_page(self):
        return self.open(self.PATH)

    def click_add(self):
        self.wait_clickable(self.ADD_BUTTON).click()
        return self

    def click_delete(self):
        self.wait_clickable(self.DELETE_BUTTON).click()
        return self

    def delete_buttons(self) -> list:
        return self.driver.find_elements(*self.DELETE_BUTTON)

    def wait_delete_count(self, expected: int, timeout: int = 10):
        self.wait.until(
            lambda d: len(d.find_elements(*self.DELETE_BUTTON)) == expected,
            message=f"Кнопок Delete не стало {expected}",
        )
        return self
