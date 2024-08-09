from behave import given, when, then
from Pages.HomePage import HomePage
from Config.Config import LoginPageData as LPD



@given('Verena is on the home page')
def step_given_user_on_home_page(context):
    context.driver.get(LPD.BASE_URL)
    context.home_page = HomePage(context.driver)

#First Scenario

@when('she selects the "Radio2" option in the radio button')
def step_selects_second_option_radio_button(context):
    context.home_page.select_second_radio_button()

@then('she should see that the "Radio2" option is selected')
def step_then_second_radio_button_is_selected(context):
    assert context.home_page.second_radio_button_is_selected(), "The 'Radio2' option is not selected" 

# Second Scenario

@when('she selects "United States (USA)" from the country menu')
def step_selects_usa__from_the_menu(context):
    context.home_page.type_in_the_country_menu("United States (USA)")
    context.home_page.select_country_from_menu("United States (USA)")

@then('she should see that the country text field value is set to "United States (USA)"')
def step_then_she_should_see_that_the_country_text_field_value_is_USA(context):
    assert context.home_page.take_actual_value() == "United States (USA)"

# Third Scenario
    
@when('she selects "Option3" from the dropdown')
def step_select_third_option_from_the_dropdown(context):
    context.home_page.select_option_from_option_dropdown("Option3")

@then('she should see that "Option3" is selected in the dropdown menu')
def step_then_should_see_the_option3_is_in_the_dropdown_field(context):
    context.home_page.take_actual_value() == "Option3"

#Fourth Scenario
    
@when('she selects "Option1" in the checkbox')
def step_selects_option1_in_the_checkbox(context):
    context.home_page.select_checkbox_option1()

@when('she selects "Option3" in the checkbox')
def step_selects_option1_in_the_checkbox(context):
    context.home_page.select_checkbox_option3()

@then('she should see that the "Option1" checkbox is checked')
def step_then_should_see_the_checkbox1_is_selected(context):
    assert context.home_page.checkbox_option1_is_selected()

@then('she should see that the "Option3" checkbox also is checked')
def step_then_should_see_the_checkbox1_is_selected(context):
    assert context.home_page.checkbox_option3_is_selected()