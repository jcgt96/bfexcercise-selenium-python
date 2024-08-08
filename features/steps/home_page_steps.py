from behave import given, when, then
from Pages.HomePage import HomePage
from Config.Config import LoginPageData as LPD



@given('Verena is on the home page')
def step_given_user_on_home_page(context):
    context.driver.get(LPD.BASE_URL)
    context.home_page = HomePage(context.driver)

@when('she selects the "Radio2" option in the radio button')
def step_selects_second_option_radio_button(context):
    context.home_page.select_second_radio_button()

@then('she should see that the "Radio2" option is selected')
def step_then_second_radio_button_is_selected(context):
    assert context.home_page.second_radio_button_is_selected(), "The 'Radio2' option is not selected" 
