Feature: Authorization
  A page with a login form that allows the user to log in to the project.

  Scenario Outline: Authorize user with valid email and password
    Given User is on the login page
    When User authorizes with <user_email> and <user_password>
    Then User is on the Home page
    And User is authorized
    Examples:
      | user_email            | user_password |
      | amiheev@urchinsys.com | 4h@TU3Wa      |

  Scenario Outline: Successful log out with user
    Given User is on the login page
    And User authorizes with <user_email> and <user_password>
    When User clicks user menu dropdown
    And User clicks the Log Out point
    Then Plextera the Login page is successfully opened
    Examples:
      | user_email            | user_password |
      | amiheev@urchinsys.com | 4h@TU3Wa      |
#
#  Scenario: Error message is shown when an invalid email is used
#    Given User is on the login page
#    When User enters an invalid value in Email address field
#    And User enters valid value in Password field
#    And User clicks the Log in button
#    Then Error message is successfully shown
#
#  Scenario: Error message is shown when an invalid password is used
#    Given User is on the login page
#    When User enters valid value in Email address field
#    And User enters an invalid value in Password field
#    And User clicks the Log in button
#    Then Error message is successfully shown
#
#  Scenario: Error message is shown when an invalid email and password is used
#    Given User is on the login page
#    When User enters an invalid value in Email address field
#    And User enters an invalid value in Password field
#    And User clicks the Log in button
#    Then Error message is successfully shown
#
#  Scenario: Error message is shown when an invalid email and password is used
#    Given User is on the login page
#    When User enters an invalid value in Email address field
#    And User enters an invalid value in Password field
#    And User clicks the Log in button
#    Then Error message is successfully shown
#
#  Scenario: Forgot password button transfers to the Forgot password page
#    Given User is on the login page
#    When User clicks the Forgot password button
#    Then Plextera the Forgot password page is successfully opened