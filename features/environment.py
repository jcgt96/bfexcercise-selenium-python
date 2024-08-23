import os

from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture
def chrome_headless_browser(context):
    options = Options()

    # Check if HEADLESS environment variable is set to "True"
    if os.getenv("HEADLESS", "False").lower() == "true":
        options.add_argument("--headless")  # Enable headless mode

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    context.browser = webdriver.Chrome(options=options)
    yield context.browser


def before_all(context):
    use_fixture(chrome_headless_browser, context)


def after_all(context):
    print("Quitting WebDriver")
    context.browser.quit()
    print("WebDriver quit")
