from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait, Select


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        ).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        ).send_keys(text)

    def get_selected_dropdown_option(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        select = Select(element)
        return select.first_selected_option.text

    def get_element_value(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        return element.get_attribute("value")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        return element.text

    def get_amount_dropdown_elements(self, by_locator):
        dropdown = self.create_a_select_element_from_locator(by_locator)
        all_options = dropdown.options
        return len(all_options)

    def select_an_option_from_dropdown(self, by_locator, option):
        dropdown = self.create_a_select_element_from_locator(by_locator)
        dropdown.select_by_visible_text(option)

    def create_a_select_element_from_locator(self, by_locator):
        dropdown_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(by_locator)
        )
        return Select(dropdown_element)

    def select_option_from_menu(self, by_locator, option):
        menu_options = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(by_locator)
        )
        for element in menu_options:
            if element.text == option:
                element.click()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_table_rows(self, table):
        return table.find_elements(By.TAG_NAME, "tr")

    def get_cell_text(self, table_locator, row_index, col_index):
        table = self.find_element(*table_locator)
        rows = self.get_table_rows(table)
        return rows[row_index].find_elements(By.TAG_NAME, "td")[col_index].text
