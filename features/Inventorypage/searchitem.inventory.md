Feature: Login and search for products in the inventory

  Scenario: User logs in and searches for products in the inventory
    Given I load the ".env" file for email and password
    When I retrieve the email "<JUBELIO_EMAIL>" and the password "<JUBELIO_PASSWORD>"
    And I navigate to the Jubelio login page
    And I enter the email "<JUBELIO_EMAIL>" and the password "<JUBELIO_PASSWORD>"
    And I click the submit button
    Then I should be redirected to the "https://app2.jubelio.com/home/getting-started" page
    And I navigate to the inventory page
    And I search for the product "Nutrimax"
    Then I should see the product "Nutrimax" in the inventory page
    And I search for the product "Blackmores"
    Then I should see the product "Blackmores" in the inventory page
