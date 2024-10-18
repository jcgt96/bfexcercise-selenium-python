import os
import re
import shutil
from datetime import datetime

import allure
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options

SCREENSHOTS_DIR = "./.run/reports/screenshots"


def before_all(context):
    clean_screenshots_folder()
    use_fixture(chrome_headless_browser, context)


def after_step(context, step):
    """Take a screenshot and attach it to the Allure report if a step fails."""
    if step.status == "failed":
        handle_alert_with_screenshot(context)
        take_screenshot(context, step.name)


def after_all(context):
    print("Quitting WebDriver")
    if context.driver:
        context.driver.quit()
    print("WebDriver quit")


# AUXILIARY METHODS AND FUNCTIONS


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


def handle_alert_with_screenshot(context):
    """Check and take a screenshot of the alert, then dismiss it."""
    try:
        alert = context.driver.switch_to.alert
        print(f"Alert detected: {alert.text}")
        alert.dismiss()  # Or alert.accept() based on your scenario
        print("Alert dismissed")
    except NoAlertPresentException:
        # No alert found, continue with the test
        pass


def take_screenshot(context, name):
    """Helper function to take a screenshot and attach it to Allure report."""

    # Create a timestamped filename for the screenshot
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{SCREENSHOTS_DIR}/{sanitize_filename(name)}_{timestamp}.png"

    # Take the screenshot using Selenium
    success = context.driver.save_screenshot(filename)

    if success:
        # Attach the screenshot to the Allure report
        with open(filename, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=f"{name} - Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

        print(f"Screenshot saved to {filename} and attached to Allure report.")
    else:
        print("Failed to save screenshot")


def sanitize_filename(input_string):
    # Remove special characters and replace them with underscores
    # This regex allows alphanumeric characters, dashes, and underscores
    sanitized = re.sub(r"[^\w\-]", "_", input_string)
    return sanitized


def clean_screenshots_folder():
    """Clean the screenshots folder by deleting all files in it."""

    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR)  # If folder doesn't exist, create it
        return  # Early exit

    # Remove all files in the folder
    for filename in os.listdir(SCREENSHOTS_DIR):
        file_path = os.path.join(SCREENSHOTS_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove file or symbolic link
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove directory
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except PermissionError:
            print(f"Permission denied: {file_path}")
        except OSError as e:
            print(f"Error occurred while deleting {file_path}. Reason: {e}")
