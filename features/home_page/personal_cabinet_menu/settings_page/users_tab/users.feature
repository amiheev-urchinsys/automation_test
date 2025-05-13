Feature: Personal cabinet - Settings page - Users tab

  Background:
    Given the user is authorized
    And the Users tab is opened in the Settings page

  Scenario: Invite new user
    When the user clicks the Invite new user button
    And enters value in the Email address field
    And selects role from the Role selector
    And clicks the Invite button
    Then the Success popup is displayed

  Scenario: Change role of another user
    When the user selects role from the Roles selector in the user row
    Then the selected role is displayed in the Roles selector

  Scenario: Deactivate user
    When the user clicks the switch in the user row
    And clicks the Disable button in the Disable confirmation popup
    Then the selected user is disabled

  Scenario: Activate user
    Given a user in the list is deactivated
    When the user clicks the switch in the user row
    And clicks the Disable button in the Enable confirmation popup
    Then the selected user is enabled


