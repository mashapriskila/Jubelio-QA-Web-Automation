Feature: Login functionality with valid credentials

  Scenario: User enters correct email and password
    Given I navigate to the Jubelio login page
    When I retrieve the email from the ".env" file and enter "<JUBELIO_EMAIL>"
    And I retrieve the password from the ".env" file and enter "<JUBELIO_PASSWORD>"
    And I click the submit button
    Then I should be redirected to the "https://app2.jubelio.com/home/getting-started" page
    And I should see the login success message
