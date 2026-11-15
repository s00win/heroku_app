from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый Page Object: общие методы ожидания и навигации."""

    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self, path: str = ""):
        self.driver.get(f"{self.BASE_URL}{path}")
        return self

    def wait_visible(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_presence_all(self, locator: tuple) -> list:
        return self.wait.until(EC.presence_of_all_elements_located(locator))