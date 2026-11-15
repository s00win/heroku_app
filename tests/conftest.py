import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    """Создаёт Chrome WebDriver перед тестом и закрывает после.

    yield — точка «передачи» браузера в тест.
    После yield — код выполнится в любом случае, даже если тест упал.
    """
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()