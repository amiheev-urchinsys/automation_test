Feature: Forgot password
  A page with a forgot password form that allows the user to send a change password request to selected email.

  Scenario: Return to login page
    Given User is on the Forgot page
    When User clicks the Back to log in button
    Then Plextera the Login page is successfully opened