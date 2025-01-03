Feature: Validate login form for empty email and password fields

  Scenario: User submits the login form without filling in email and password
    Given I navigate to the login page
    When I enter an email "example@mail.com" and a password "123456"
    And I delete both the email and password fields slowly
    Then the "Email harus diisi" message should be displayed
    And the "Password harus diisi" message should be displayed
