from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

email = os.getenv('JUBELIO_EMAIL')
password = os.getenv('JUBELIO_PASSWORD')

driver = webdriver.Edge()

def login_jubelio(username, password):
    try:
        driver.get('https://app2.jubelio.com/login')
        driver.maximize_window()
        driver.find_element(By.NAME, 'email').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        
        if driver.current_url == "https://app2.jubelio.com/home/getting-started":
            print("Login successful!")
        else:
            print("Login failed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_item_with_details():
    try:
        # Navigate to the inventory review page to create a new item
        driver.get('https://app2.jubelio.com/home/inventory/review')
        time.sleep(3)

        # Click the "Tambah Baru" button to add a new item
        tambah_baru_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Tambah Baru')]")
        tambah_baru_button.click()
        time.sleep(3)

        # Find label elements containing specific text
        labels = driver.find_elements(By.XPATH, "//label[contains(text(), 'Nama') or contains(text(), 'Deskripsi') or contains(text(), 'Kategori Barang')]")

        # Iterate through each label and input values based on the label text
        for label in labels:
            label_text = label.text.strip()

            if "Nama" in label_text:
                input_field = label.find_element(By.XPATH, ".//following-sibling::input[@type='text']")
                input_field.send_keys('Blackmores Multivitamin')

            elif "Deskripsi" in label_text:
                textarea_field = label.find_element(By.XPATH, ".//following-sibling::textarea")
                textarea_field.send_keys('Multivitamin yang berguna untuk menjaga imunitas tubuh')

            elif "Kategori Barang" in label_text:
                input_field = label.find_element(By.XPATH, ".//following-sibling::input[@type='text']")
                input_field.send_keys('Kesehatan')

        time.sleep(2)

        # Click the "Simpan" button to save the item
        simpan_button = driver.find_element(By.CLASS_NAME, 'ladda-button.btn.btn-primary.std-btn-width')
        simpan_button.click()
        time.sleep(3)

        # Go to the inventory page to check if the item appears
        driver.get('https://app2.jubelio.com/home/inventory')
        time.sleep(3)

        # Verify if the new item appears on the inventory page
        item_name = 'Blackmores Multivitamin'
        product_elements = driver.find_elements(By.XPATH, f"//div[contains(@class, 'react-grid-Canvas')]//div[contains(text(), '{item_name}')]")

        if product_elements:
            print(f"Item '{item_name}' found on the inventory page!")
        else:
            print(f"Item '{item_name}' not found on the inventory page.")

    except Exception as e:
        print(f"An error occurred while creating the item or verifying the inventory: {e}")

def main():
    login_jubelio(email, password)
    create_item_with_details()

main()
