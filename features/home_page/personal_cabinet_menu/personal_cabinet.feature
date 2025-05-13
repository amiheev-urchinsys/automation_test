Feature: Personal cabinet

  Background:
    Given the user is authorized

  Scenario: Navigate to the Settings page
    When the user clicks the personal cabinet selector in the left sidebar
    And the user clicks the Settings point from the dropdown list
    Then the Settings page is displayed

  Scenario: Navigate to the Admin console page
    When the user clicks the personal cabinet selector in the left sidebar
    And the user clicks the Admin console point from the dropdown list
    Then the Admin console page is displayed

  Scenario: Log out
    When the user clicks the personal cabinet selector in the left sidebar
    And the user clicks the Log out point from the dropdown list
    Then the Login page is displayed