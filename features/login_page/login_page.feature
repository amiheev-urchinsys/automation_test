Feature: Authorization
  A page with a login form that allows the user to log in to the project.

  Scenario Outline: Authorize user with valid email and password
    Given User is on the login page
    When User authorizes with <user_email> and <user_password>
    Then User is on the Home page
    And User is authorized
    Examples:
      | user_email              | user_password |
      | amiheev@urchinsys.com   | 4h@TU3Wa      |
      | amiheev+1@urchinsys.com | h29j$KHg6p    |
      | amiheev+2@urchinsys.com | X6@iA8QvAC    |
      | amiheev+3@urchinsys.com | aSN9o?imjT    |
#
#
#  Scenario Outline: Successful log out with user
#    Given User is on the login page
#    And User authorizes with <user_email> and <user_password>
#    When User clicks user menu dropdown
#    And User clicks the Log Out point
#    Then Plextera the Login page is successfully opened
#    Examples:
#      | user_email              | user_password |
#      | amiheev@urchinsys.com   | 4h@TU3Wa      |
#      | amiheev+1@urchinsys.com | h29j$KHg6p    |
#      | amiheev+2@urchinsys.com | X6@iA8QvAC    |
#      | amiheev+3@urchinsys.com | aSN9o?imjT    |
#
#  Scenario Outline: Error message is shown when an invalid credentials are used
#    Given User is on the login page
#    When User authorizes with <user_email> and <user_password>
#    Then Error message is successfully shown <error_text>
#    Examples:
#      | user_email            | user_password | error_text          |
#      | tt@tt.tt              | 4h@TU3Wa      | Invalid credentials |
#      | amiheev@urchinsys.com | 111111        | Invalid credentials |
#      | tt@tt.tt              | 111111        | Invalid credentials |
#
#  Scenario: Forgot password button transfers to the Forgot password page
#    Given User is on the login page
#    When User clicks the Forgot password button
#    Then Plextera the Forgot password page is successfully opened