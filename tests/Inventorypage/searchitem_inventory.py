from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        time.sleep(10)
        if driver.current_url == "https://app2.jubelio.com/home/getting-started":
            print("Login successful!")
        else:
            print("Login failed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_product(product_name):
    try:
        driver.get('https://app2.jubelio.com/home/inventory')
        time.sleep(5)
        search_input = driver.find_element(By.XPATH, "//input[@type='text']")  # Adjust XPath if necessary
        search_input.clear()
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)
        products = driver.find_elements(By.XPATH, f"//td[contains(text(), '{product_name}')]")
        if products:
            print(f"Product '{product_name}' found!")
        else:
            print(f"Product '{product_name}' not found.")
    except Exception as e:
        print(f"An error occurred while searching for {product_name}: {e}")

def main():
    login_jubelio(email, password)
    search_product('Nutrimax')
    search_product('Blackmores')
    time.sleep(5)
    driver.quit()

main()
