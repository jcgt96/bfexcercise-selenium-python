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