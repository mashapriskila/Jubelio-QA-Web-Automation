from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Edge()

def delete_slowly(element, num_characters, delay=0.2):
    for _ in range(num_characters):
        element.send_keys(Keys.BACKSPACE)
        time.sleep(delay)

def validate_empty_email_and_password():
    try:
        driver.get('https://app2.jubelio.com/login')
        driver.maximize_window()

        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')

        # Type email and password quickly
        email_input.send_keys('example@gmail.com')
        password_input.send_keys('123456')

        time.sleep(1)

        # Delete the email and password slowly, one character at a time
        delete_slowly(email_input, len('example@gmail.com'))
        delete_slowly(password_input, len('123456'))

        time.sleep(2)

        email_required_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Email harus diisi')]")
        password_required_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Password harus diisi')]")

        if email_required_message:
            print("Email validation works: 'Email harus diisi.' message is displayed.")
        if password_required_message:
            print("Password validation works: 'Password harus diisi.' message is displayed.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(3)
        driver.quit()

validate_empty_email_and_password()
