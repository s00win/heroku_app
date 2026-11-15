from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    PATH = "/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def open_page(self):
        return self.open(self.PATH)

    def _select(self) -> Select:
        return Select(self.wait_visible(self.DROPDOWN))

    def get_all_options(self) -> list[str]:
        return [opt.text for opt in self._select().options]

    def select_by_index(self, index: int):
        self._select().select_by_index(index)
        return self

    def selected_text(self) -> str:
        return self._select().first_selected_option.text