Feature: Advanced User Exercises
  As a User
  I want to test all the advanced exercises
  So that I can enhance my skills with practical applications

  Background: Open the home page
    Given Verena is on the home page

    #=============================================================================

  #@skip
  Scenario: Displaying the Contextual Menu via Mouse Hover
    When she hover over the "Mouse Hover" button
    Then she should see the contextual menu

#@skip
  Scenario: Navigating to a Support Link Within an Iframe
    When she navigates to the "Job Support" link inside the iframe
    Then she should see a page titled "JOB SUPPORT" within the iframe

  @newwindow
  Scenario: Opening and Verifying a Blog Page in a New Window
    When she clicks on the "Open Window" button
    And she clicks the "Blog" link in the new window
    Then she should see a page titled "Mindblown: a blog about philosophy."
    And she should return to the main page after closing the new window

  @newwindow2
  Scenario: Opening and Verifying a Blog Page in a New Tab
    When she clicks on the "New Tab" button
    And she clicks the "Blog" link in the new tab
    Then she should see a page titled "Mindblown: a blog about philosophy."
    And she should returns to the main page after closing the new tab
