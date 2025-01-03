Feature: Login and attempt to create an item with missing fields

  Scenario: User logs in and attempts to create an item with missing fields
    Given I load the ".env" file for email and password
    When I retrieve the email "<JUBELIO_EMAIL>" and the password "<JUBELIO_PASSWORD>"
    And I navigate to the Jubelio login page
    And I enter the email "<JUBELIO_EMAIL>" and the password "<JUBELIO_PASSWORD>"
    And I click the submit button
    Then I should be redirected to the "https://app2.jubelio.com/home/getting-started" page
    And I navigate to the inventory review page
    And I click the "Tambah Baru" button to add a new item
    And I leave all the fields empty
    And I click the "Simpan" button to save the item
    Then I should see the following error messages:
      | Nama harus diisi.                                                              |
      | Deskripsi harus diisi.                                                         |
      | Harga Default harus lebih besar atau sama dengan 100.                          |
      | Kategori barang harus diisi.                                                   |
      | Berat Paket (Gram) harus diisi.                                                |
