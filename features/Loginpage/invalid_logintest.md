Feature: Login functionality with invalid credentials

  Scenario: User enters incorrect email or password
    Given I navigate to the Jubelio login page
    When I enter the email "emailsalah@gmail.com" and the password "123456"
    And I click the submit button
    Then I should see the error message "Password atau email anda salah"
