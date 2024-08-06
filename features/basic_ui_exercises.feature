Feature: Practicing Basic User Interactions
  As a User
  I want to test various basic exercises
  So that I can enhance my practical skills with foundational interactions

  Background: Accessing the Home Page
    Given Verena is on the home page

    #=============================================================================

  #@skip
  Scenario: Selecting an Option in a Radio Button
    When she select the "Radio2" option in the radio button
    Then she should see that the "Radio2" option is selected