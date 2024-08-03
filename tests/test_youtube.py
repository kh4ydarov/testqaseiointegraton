import pytest
from selenium.webdriver.common.by import By
from qase.pytest import qase


@qase.id(1)  # Ensure this ID matches the ID of the test case in Qase.io
@qase.title("test_auto")
@qase.fields(
    ("severity", "critical"),
    ("priority", "high"),
    ("layer", "unit"),
    ("description", "Try to login to Qase TestOps using login and password"),
    ("preconditions", "*Precondition 1*. Markdown is supported."),
)
def test_open_page(browser):
    browser.find_element(By.CSS_SELECTOR, '#guide-button').click()
