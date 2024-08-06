from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()  # o el WebDriver de tu elección

def after_all(context):
    context.driver.quit()
