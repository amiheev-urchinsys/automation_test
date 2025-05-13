Feature: Home page
  Elements or functional that that can be accessed from any page

  Background:
    Given the user is authorized

  Scenario: Navigate to the Workflows page
    When the user clicks the Workflows point in the left sidebar
    Then the Workflows page is displayed

  Scenario: Navigate to the Web automations page
    When the user clicks the Web automations point in the left sidebar
    Then the Web automations page is displayed

  Scenario: Navigate to the Documents Insights page
    When the user clicks the Documents Insights point in the left sidebar
    Then the Documents Insights page is displayed

  Scenario: Navigate to the SIDES page
    When the user clicks the SIDES point in the left sidebar
    Then the SIDES page is displayed

  Scenario: Navigate to the Datastores page
    When the user clicks the Datastores point in the left sidebar
    Then the Datastores page is displayed

  Scenario: Navigate to the Forms page
    When the user clicks the Forms point in the left sidebar
    Then the Forms page is displayed

  Scenario: Open personal cabinet menu
    When the user clicks the personal cabinet selector in the left sidebar
    Then the dropdown list is displayed





