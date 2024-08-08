from .BasePage import BasePage
from Resources.Locators import HomePageLocators as HPL
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    def select_second_radio_button(self):
        self.do_click(HPL.second_radio_button)

    def second_radio_button_is_selected(self):
        return self.find_element(*HPL.second_radio_button).is_selected()
    
    def type_in_the_country_menu(self, country):
        self.do_send_keys(HPL.country_menu, country)

    def select_country_from_menu(self, country):
        self.select_option_from_menu(HPL.country_menu, country)

    def take_actual_value(self):
        country_field = self.find_element(*HPL.country_menu)
        return country_field.get_attribute("value")
    
    def select_option_from_option_dropdown(self,dropdown_option):
        self.select_an_option_from_dropdown(HPL.option_dropdown, dropdown_option)