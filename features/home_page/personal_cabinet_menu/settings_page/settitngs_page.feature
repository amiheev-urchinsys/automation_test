Feature: Personal cabinet - Settings page

  Background:
    Given the user is authorized
    And the Settings page is open in the Personal Cabinet

  Scenario: Navigate to the Account tab
    Given the API tab is open in the Settings page
    When the user clicks the Account point in the User Settings block
    Then the Account tab is displayed

  Scenario: Navigate to the Notification tab
    When the user clicks the Notification point in the User Settings block
    Then the Notification tab is displayed

  Scenario: Navigate to the API tab
    When the user clicks the API point in the User Settings block
    Then the API tab is displayed

  Scenario: Navigate to the General tab
    When the user clicks the General point in the Workspace Settings block
    Then the General tab is displayed

  Scenario: Navigate to the Users tab
    When the user clicks the Users point in the Workspace Settings block
    Then the Users tab is displayed

  Scenario: Navigate to the Billing tab
    When the user clicks the Billing point in the Workspace Settings block
    Then the Billing tab is displayed