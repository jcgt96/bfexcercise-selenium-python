from src.main.resources.locators import (
    SECOND_RADIO_BUTTON,
    COUNTRY_MENU,
    OPTION_DROPDOWN,
    CHECKBOX_1,
    CHECKBOX_3,
)
from .base_page import BasePage


class HomePage(BasePage):

    def select_second_radio_button(self):
        self.do_click(SECOND_RADIO_BUTTON)

    def second_radio_button_is_selected(self):
        return self.find_element(*SECOND_RADIO_BUTTON).is_selected()

    def type_in_the_country_menu(self, country):
        self.do_send_keys(COUNTRY_MENU, country)

    def select_country_from_menu(self, country):
        self.select_option_from_menu(COUNTRY_MENU, country)

    def take_actual_value(self):
        return self.get_element_value(COUNTRY_MENU)

    def select_option_from_option_dropdown(self, dropdown_option):
        self.select_an_option_from_dropdown(OPTION_DROPDOWN, dropdown_option)

    def take_actual_value_from_dropdown(self):
        return self.get_selected_dropdown_option(OPTION_DROPDOWN)

    def select_checkbox_option1(self):
        self.do_click(CHECKBOX_1)

    def select_checkbox_option3(self):
        self.do_click(CHECKBOX_3)

    def checkbox_option1_is_selected(self):
        return self.find_element(*CHECKBOX_1).is_selected()

    def checkbox_option3_is_selected(self):
        return self.find_element(*CHECKBOX_3).is_selected()
