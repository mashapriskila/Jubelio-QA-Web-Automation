Feature: Validate email format and password length on the login form

  Scenario: User enters an invalid email format and a password with incorrect length
    Given I navigate to the login page
    When I enter the email "invalidemailformat" and the password "1234"
    And I delete the last 2 characters of the email and 1 character of the password
    Then the "Format Email tidak valid." message should be displayed
    And the "Password harus di antara 6 dan 30." message should be displayed
