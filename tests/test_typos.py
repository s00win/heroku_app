import pytest
from pages.typos_page import TyposPage


@pytest.mark.advanced
def test_paragraph_has_valid_text(browser):
    page = TyposPage(browser).open_page()
    text = page.content_text().lower()

    assert "typo" in text or "tpyo" in text, (
        f"В тексте нет 'typo' или 'tpyo': {text!r}"
    )


@pytest.mark.advanced
def test_paragraph_is_not_empty(browser):
    page = TyposPage(browser).open_page()
    assert len(page.content_text()) > 0
