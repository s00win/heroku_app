from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TyposPage(BasePage):
    PATH = "/typos"
    PARAGRAPH = (By.TAG_NAME, "p")

    def open_page(self):
        return self.open(self.PATH)

    def all_paragraphs(self) -> list[str]:
        return [p.text.strip() for p in self.wait_presence_all(self.PARAGRAPH)]

    def content_text(self) -> str:
        paragraphs = self.all_paragraphs()
        return paragraphs[-1] if paragraphs else ""
