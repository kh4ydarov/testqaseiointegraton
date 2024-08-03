import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Uncomment if you want to run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.page_load_strategy = 'eager'
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


@pytest.fixture(scope="function", autouse=True)
def browser():
    options = set_chrome_options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1366, 768)
    driver.get('https://youtube.com')
    yield driver
    driver.quit()
