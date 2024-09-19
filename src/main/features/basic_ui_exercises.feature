Feature: Practicing Basic User Interactions
    As a User
    I want to test various basic exercises
    So that I can enhance my practical skills with foundational interactions

    Background: Accessing the Home Page
        Given Verena is on the home page

    #=============================================================================

  #@skip
    Scenario: Selecting an Option in a Radio Button
        When she selects the "radio2" option in the radio button
        Then she should see that the "radio2" option is selected

#@skip
    Scenario: Choosing a Country from a Dropdown Menu
        When she selects "United States (USA)" from the country menu
        Then she should see that the country text field value is set to "United States (USA)"

#@skip
    Scenario: Selecting an Option from a Dropdown Menu
        When she selects "Option3" from the dropdown
        Then she should see that "Option3" is selected in the dropdown menu

  #@skip
    Scenario: Verifying Multiple Checkbox Selections
        When she selects "Option1" in the checkbox
        And she selects "Option3" in the checkbox
        Then she should see that the "Option1" checkbox is checked
        And she should see that the "Option3" checkbox also is checked

  #@skip
  Scenario: Displaying a Custom Alert with the Name
    When she triggers an Alert Dialog with the name "JUANK"
    Then she should see an Alert Dialog with the text "Hello JUANK, share this practice page and share your knowledge"


  Scenario: Displaying a Custom Confirm Dialog with a Custom Name
    When she triggers a Confirmation Dialog for the name "JUANK"
    Then she should see a Confirmation Dialog with the prompt "Hello JUANK, Are you sure you want to confirm?"

  Scenario: Checking the Value of the Third item in the Price Table
    When she reads the third value listed in the price table
    Then she should see that the third price is "30"

  Scenario: Hiding a Visible Text Box
    When Verena can see that the "HideShow Example" text box is visible
    And she requests to hide the "HideShow Example" text box
    Then she should see the text box become hidden

  Scenario: Toggling Visibility of a Text Box
    When Verena can see that the "HideShow Example" text box is visible
    And she requests to hide the "HideShow Example" text box
    And she requests to show it again
    Then she should see the text box become visible again
