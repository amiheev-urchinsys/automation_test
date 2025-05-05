Feature: Authorization
  A page with a login form that allows the user to log in to the project.

  Scenario Outline: Authorize user with valid email and password
    Given User is on the login page
    When User authorizes with <user_email> and <user_password>
    Then User is on the Home page and the greetings text is visible
    Examples:
      | user_email            | user_password |
      | amiheev@urchinsys.com | 4h@TU3Wa      |