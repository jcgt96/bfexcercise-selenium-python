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
HOVER_BUTTON: tuple[str, str] = (By.XPATH, "//button[@id='mousehover']")
CONTEXTUAL_MENU: tuple[str, str] = (By.XPATH, "//a[normalize-space()='Top']")
FRAME: tuple[str, str] = (By.XPATH, "//*[@id='courses-iframe']")
JOB_SUPPORT_OPTION: tuple[str, str] = (By.LINK_TEXT, "Job Support")
JOB_SUPPORT_TITLE_PAGE: tuple[str, str] = (
    By.XPATH,
    "//h1[normalize-space()='Job Support']",
)
OPEN_WINDOW_BUTTON: tuple[str, str] = (By.XPATH, "//button[@id='openwindow']")
BLOG_LINK: tuple[str, str] = (By.XPATH, "//a[text()='Blog']")
NEW_WINDOW_TITLE: tuple[str, str] = (
    By.XPATH,
    "//h1[@class='alignwide wp-block-heading']",
)
NEW_TAB_BUTTON: tuple[str, str] = (By.XPATH, "//a[@id='opentab']")
