from selenium.webdriver.common.by import By

SECOND_RADIO_BUTTON: tuple[str, str] = (By.XPATH, "//input[@value='radio2']")
COUNTRY_MENU: tuple[str, str] = (By.XPATH, "//input[@id='autocomplete']")
OPTION_DROPDOWN: tuple[str, str] = (By.XPATH, "//select[@id='dropdown-class-example']")
CHECKBOX_1: tuple[str, str] = (By.XPATH, "//input[@id='checkBoxOption1']")
CHECKBOX_3: tuple[str, str] = (By.XPATH, "//input[@id='checkBoxOption3']")
NAME_INPUT: tuple[str, str] = (By.XPATH, "//input[@id='name']")
ALERT_BUTTON: tuple[str, str] = (By.XPATH, "//input[@id='alertbtn']")
CONFIRM_BUTTON: tuple[str, str] = (By.XPATH, "//input[@id='confirmbtn']")
TABLE: tuple[str, str] = (By.XPATH, "//div[@class='left-align']//table[@id='product']")
TEXT_BOX_INPUT: tuple[str, str] = (By.XPATH, "//input[@id='displayed-text']")
SHOW_BUTTON: tuple[str, str] = (By.XPATH, "//input[@id='show-textbox']")
HIDE_BUTTON: tuple[str, str] = (By.XPATH, "//input[@id='hide-textbox']")
