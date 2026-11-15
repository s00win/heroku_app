from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InputsPage(BasePage):
    PATH = "/inputs"
    INPUT = (By.TAG_NAME, "input")

    def open_page(self):
        return self.open(self.PATH)

    def input_field(self):
        return self.wait_visible(self.INPUT)

    def type_text(self, text: str):
        field = self.input_field()
        field.clear()
        field.send_keys(text)
        return self

    def press_key(self, key):
        self.input_field().send_keys(key)
        return self

    def value(self) -> str:
        return self.input_field().get_attribute("value")