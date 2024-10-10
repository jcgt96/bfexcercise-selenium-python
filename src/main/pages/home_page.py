from selenium.webdriver.common.by import By
from src.main.resources.locators import (
    SECOND_RADIO_BUTTON,
    COUNTRY_MENU,
    OPTION_DROPDOWN,
    CHECKBOX_1,
    CHECKBOX_3,
    NAME_INPUT,
    ALERT_BUTTON,
    CONFIRM_BUTTON,
    TABLE,
    TEXT_BOX_INPUT,
    SHOW_BUTTON,
    HIDE_BUTTON,
    HOVER_BUTTON,
    CONTEXTUAL_MENU,
    FRAME,
    JOB_SUPPORT_OPTION,
    JOB_SUPPORT_TITLE_PAGE,
    OPEN_WINDOW_BUTTON,
    PRE_LOADER,
    BLOG_LINK,
    NEW_WINDOW_TITLE,
    NEW_TAB_BUTTON,
)
from .base_page import BasePage


class HomePage(BasePage):

    def select_radio_button(self, radio_button_value):
        radio_button_lc = (By.XPATH, f'//input[@value="{radio_button_value}"]')
        self.do_click(radio_button_lc)

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

    def trigger_customized_alert(self, name):
        self.do_send_keys(NAME_INPUT, name)
        self.do_click(ALERT_BUTTON)

    def trigger_customized_confirmation(self, name):
        self.do_send_keys(NAME_INPUT, name)
        self.do_click(CONFIRM_BUTTON)

    def get_tex_of_alert(self):
        alert_text = self.get_alert_text()
        return alert_text

    def dismiss_alert_dialog(self):
        self.dismiss_alert()

    def write_in_text_box(self, text):
        self.do_send_keys(TEXT_BOX_INPUT, text)

    def show_text_box(self):
        self.do_click(SHOW_BUTTON)

    def hide_text_box(self):
        self.do_click(HIDE_BUTTON)

    def get_text_box_element(self):
        text_box_element = self.find_element(*TEXT_BOX_INPUT)
        return text_box_element

    def get_text_box_text(self):
        text_box_text = self.get_element_value(TEXT_BOX_INPUT)
        return text_box_text

    def get_specific_cell_text(self, row_index, col_index):
        return self.get_cell_text(TABLE, row_index, col_index)

    def hover_hover_button(self):
        self.do_hover(HOVER_BUTTON)

    def contextual_menu_is_displayed(self):
        return self.find_element(*CONTEXTUAL_MENU).is_displayed()

    def switch_home_iframe(self):
        self.switch_to_iframe(FRAME)

    def go_to_job_support_link(self):
        self.do_click(JOB_SUPPORT_OPTION)

    def get_frame_page_title(self):
        return self.get_element_text(JOB_SUPPORT_TITLE_PAGE)

    def return_home_page_from_frame(self):
        self.return_from_iframe()

    def clicks_open_window_button(self):
        self.do_click(OPEN_WINDOW_BUTTON)

    def switch_to_home_new_window(self):
        self.switch_to_new_window()
        self.wait_for_element_to_disappear(PRE_LOADER)

    def switch_to_home_new_tab(self):
        self.switch_to_tab(1)
        self.wait_for_element_to_disappear(PRE_LOADER)

    def clicks_blog_link(self):
        self.do_click(BLOG_LINK)

    def get_new_window_title(self):
        return self.get_element_text(NEW_WINDOW_TITLE)

    def close_and_return_to_home_page(self):
        self.close_window()
        self.return_to_main_window()

    def close_tab_and_return_to_home_page(self):
        self.close_window()
        self.switch_to_tab(0)

    def click_new_tab_button(self):
        self.do_click(NEW_TAB_BUTTON)
