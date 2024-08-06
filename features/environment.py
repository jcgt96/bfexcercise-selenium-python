from selenium import webdriver

def before_all(context):
    print("Initializing WebDriver")
    context.driver = webdriver.Chrome()
    print("WebDriver initialized")

def after_all(context):
    print("Quitting WebDriver")
    context.driver.quit()
    print("WebDriver quit")
