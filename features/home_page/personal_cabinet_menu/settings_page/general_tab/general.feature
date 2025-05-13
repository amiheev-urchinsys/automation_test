Feature: Personal cabinet - Settings page - General tab

  Background:
    Given the user is authorized
    And the General tab is opened in the Settings page

  Scenario: Change the Company name field value
    When the user deletes the value from the Company name field
    And enters the value in the Company name field
    And clicks the Update button
    Then the Success popup is displayed

  Scenario: Add the Company URL field value
    When the user enters the value from the Company URL field
    And clicks the Update button
    Then the Success popup is displayed

  Scenario: Change the Company URL field value
    Given the Company URL field is populated
    When the user deletes the value from the Company URL field
    And enteres the value in the Company URL field
    And clicks the Update button
    Then the Success popup is displayed

  Scenario: Change the Size limit field value
    When the user deletes the value from the Size limit field
    And enteres the value in the Size limit field
    Then the entered value is displayed in the Size limit field

  Scenario: Change the Remove Data After selector value
    When the user clicks the Remove Data After selector
    And selects the value from the dropdown list
    Then the selected value is displayed in the Remove Data After selector
