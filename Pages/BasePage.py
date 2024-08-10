from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text)

    def get_selected_dropdown_option(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        select = Select(element)
        return select.first_selected_option.text


    def get_amount_dropdown_elements(self, by_locator):
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator)
        )
        dropdown = Select(dropdown_element)
        all_options = dropdown.options
        return len(all_options)

    def select_an_option_from_dropdown(self, by_locator, option):
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(option)

    def select_option_from_menu(self, by_locator, option):
        menu_options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(by_locator)
        )
        for element in menu_options:
            if element.text == option:
                element.click()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)
