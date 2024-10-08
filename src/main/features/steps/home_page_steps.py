from behave import given, when, then, step

from src.main.config.config import BASE_URL
from src.main.pages.home_page import HomePage


@given("Verena is on the home page")
def step_given_user_on_home_page(context):
    context.browser.get(BASE_URL)
    context.home_page = HomePage(context.browser)


# First Scenario


@when('she selects the "{radio_option}" option in the radio button')
def step_selects_second_option_radio_button(context, radio_option):
    context.home_page.select_radio_button(radio_option)


@then('she should see that the "radio2" option is selected')
def step_then_second_radio_button_is_selected(context):
    assert (
        context.home_page.second_radio_button_is_selected()
    ), "The 'Radio2' option is not selected"


# Second Scenario


@when('she selects "{country_name}" from the country menu')
def step_selects_country_from_the_menu(context, country_name):
    context.home_page.type_in_the_country_menu(country_name)
    context.home_page.select_country_from_menu(country_name)


@then('she should see that the country text field value is set to "{country_name}"')
def step_then_she_should_see_that_the_country_text_field_value_is(
    context, country_name
):
    assert context.home_page.take_actual_value() == country_name


# Third Scenario


@when('she selects "{dropbox_option}" from the dropdown')
def step_select_third_option_from_the_dropdown(context, dropbox_option):
    context.home_page.select_option_from_option_dropdown(dropbox_option)


@then('she should see that "{dropbox_option}" is selected in the dropdown menu')
def step_then_should_see_the_option_is_in_the_dropdown_field(context, dropbox_option):
    assert context.home_page.take_actual_value_from_dropdown() == dropbox_option


# Fourth Scenario


@when('she selects "Option1" in the checkbox')
def step_selects_option1_in_the_checkbox(context):
    context.home_page.select_checkbox_option1()


@when('she selects "Option3" in the checkbox')
def step_selects_option3_in_the_checkbox(context):
    context.home_page.select_checkbox_option3()


@then('she should see that the "Option1" checkbox is checked')
def step_then_should_see_the_checkbox1_is_selected(context):
    assert context.home_page.checkbox_option1_is_selected()


@then('she should see that the "Option3" checkbox also is checked')
def step_then_should_see_the_checkbox3_is_selected(context):
    assert context.home_page.checkbox_option3_is_selected()


# Fifth Scenario
@when('she triggers an Alert Dialog with the name "{name}"')
def step_when_she_triggers_an_alert_dialog_with_a_name(context, name):
    context.home_page.trigger_customized_alert(name)


@then('she should see an Alert Dialog with the text "{message}"')
def step_check_message_in_alert(context, message):
    assert context.home_page.get_tex_of_alert() == message
    context.home_page.dismiss_alert_dialog()


# Sixth Scenario
@when('she triggers a Confirmation Dialog for the name "{name}"')
def step_when_she_triggers_a_confirmation_dialog_with_a_name(context, name):
    context.home_page.trigger_customized_confirmation(name)


@then('she should see a Confirmation Dialog with the prompt "{prompt}"')
def step_check_prompt_in_confirmation_dialog(context, prompt):
    assert context.home_page.get_tex_of_alert() == prompt
    context.home_page.dismiss_alert_dialog()


# Seventh Scenario
@when("she reads the third value listed in the price table")
def step_read_third_value_in_price_col(context):
    context.third_value = context.home_page.get_specific_cell_text(3, 2)


@then('she should see that the third price is "{price}"')
def step_check_third_price(context, price):
    assert context.third_value == price


# Eigth Scenario
@when('Verena can see that the "{text}" text box is visible')
def step_can_see_visible_text(context, text):
    context.home_page.write_in_text_box(text)
    context.home_page.show_text_box()
    assert context.home_page.get_text_box_text() in text


@when('she requests to hide the "HideShow Example" text box')
def step_hide_text_box(context):
    context.home_page.hide_text_box()


@then("she should see the text box become hidden")
def step_verify_text_box_is_hidden(context):
    assert not context.home_page.get_text_box_element().is_displayed()


# Ninth Scenario
@when("she requests to show it again")
def step_show_text_box(context):
    context.home_page.show_text_box()


@then("she should see the text box become visible again")
def step_verify_text_box_is_visible(context):
    assert context.home_page.get_text_box_element().is_displayed()


# Advanced Exercises


# First Exercise
@when('she hover over the "Mouse Hover" button')
def step_hover_the_hover_button(context):
    context.home_page.hover_hover_button()


@then("she should see the contextual menu")
def step_contextual_menu_is_displayed(context):
    assert context.home_page.contextual_menu_is_displayed()


# Second Exercise
@when('she navigates to the "Job Support" link inside the iframe')
def step_navigates_iframe_job_support_page(context):
    context.home_page.switch_home_iframe()
    context.home_page.go_to_job_support_link()


@then('she should see a page titled "{title_name}" within the iframe')
def step_title_value_is_expected(context, title_name):
    current_page_title = context.home_page.get_frame_page_title()
    assert current_page_title == title_name
    context.home_page.return_home_page_from_frame()


# Third Exercise
@when('she clicks on the "Open Window" button')
def step_click_new_window_button(context):
    context.home_page.clicks_open_window_button()


@when('she clicks the "Blog" link in the new window')
def step_clicks_blog_link_new_window(context):
    context.home_page.switch_to_home_new_window()
    context.home_page.clicks_blog_link()


@then('she should see a page titled "{title}"')
def step_title_window_is_expected(context, title):
    assert context.home_page.get_new_window_title() == title


@step("she should return to the main page after closing the new window")
def step_close_and_return_to_main_page(context):
    context.home_page.close_and_return_to_home_page()


# Fourth Exercise
@when('she clicks on the "New Tab" button')
def step_click_new_tab_button(context):
    context.home_page.click_new_tab_button()


@when('she clicks the "Blog" link in the new tab')
def step_click_blog_new_tab(context):
    context.home_page.switch_to_home_new_tab()
    context.home_page.clicks_blog_link()


@step("she should returns to the main page after closing the new tab")
def step_return_to_main_tab(context):
    context.home_page.close_and_return_to_home_page()
