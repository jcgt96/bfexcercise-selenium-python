Feature: Practicing Basic User Interactions
  As a User
  I want to test various basic exercises
  So that I can enhance my practical skills with foundational interactions

  Background: Accessing the Home Page
    Given Verena is on the home page

    #=============================================================================

  #@skip
  Scenario: Selecting an Option in a Radio Button
    When she selects the "Radio2" option in the radio button
    Then she should see that the "Radio2" option is selected

#@skip
  Scenario: Choosing a Country from a Dropdown Menu
    When she selects "United States (USA)" from the country menu
    Then she should see that the country text field value is set to "United States (USA)"

#@skip
  Scenario: Selecting an Option from a Dropdown Menu
    When she selects "Option3" from the dropdown
    Then she should see that "Option3" is selected in the dropdown menu