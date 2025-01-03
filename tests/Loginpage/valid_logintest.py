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

        time.sleep(10) 
        
        if driver.current_url == "https://app2.jubelio.com/home/getting-started":
            print("Login successful!")
        else:
            print("Login failed!")

    except Exception as e:
        print(f"An error occurred: {e}")

    
login_jubelio(email, password)
