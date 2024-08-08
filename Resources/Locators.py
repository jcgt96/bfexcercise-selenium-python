from selenium.webdriver.common.by import By

class HomePageLocators:
    second_radio_button = (By.XPATH, "//input[@value='radio2']")
    country_menu = (By.XPATH, "//input[@id='autocomplete']")
    option_dropdown = (By.XPATH, "//select[@id='dropdown-class-example']")
    