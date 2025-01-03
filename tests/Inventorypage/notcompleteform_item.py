from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os


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

def create_empty_item():
    try:
        
        driver.get('https://app2.jubelio.com/home/inventory/review')
        time.sleep(2)

        
        tambah_baru_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Tambah Baru')]")
        tambah_baru_button.click()
        time.sleep(4)

        
        simpan_button = driver.find_element(By.CLASS_NAME, 'ladda-button.btn.btn-primary.std-btn-width')
        simpan_button.click()
        time.sleep(3)

        error_div = driver.find_element(By.CLASS_NAME, 'app-alert.alert.alert-danger.alert-dismissable')

        
        error_text = error_div.text

        
        expected_errors = [
            "Nama harus diisi.",
            "Deskripsi harus diisi.",
            "Harga Default harus lebih besar atau sama dengan 100.",
            "Kategori barang harus diisi.",
            "Berat Paket (Gram) harus diisi."
        ]
        
        for error in expected_errors:
            if error in error_text:
                print(f"Expected error message found: {error}")
            else:
                print(f"Expected error message not found: {error}")

    except Exception as e:
        print(f"An error occurred during item creation: {e}")

def main():
    login_jubelio(email, password)
    create_empty_item()

main()
