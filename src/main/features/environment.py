import os

from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def after_all(context):
    print("Quitting WebDriver")
    if context.driver:
        context.driver.quit()
    print("WebDriver quit")

@fixture
def chrome_headless_browser(context):
    options = Options()

    # Check if HEADLESS environment variable is set to "True"
    if os.getenv("HEADLESS", "False").lower() == "true":
        options.add_argument("--headless")  # Enable headless mode

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    context.driver = webdriver.Chrome(options=options)
    yield context.driver


def before_all(context):
    use_fixture(chrome_headless_browser, context)


