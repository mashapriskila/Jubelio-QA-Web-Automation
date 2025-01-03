from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Edge()

def slow_type(element, text, delay=0.2):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

def delete_last_characters(element, num_characters, delay=0.2):
    for _ in range(num_characters):
        element.send_keys(Keys.BACKSPACE)
        time.sleep(delay)

def validate_email_and_password():
    try:
        driver.get('https://app2.jubelio.com/login')
        driver.maximize_window()

        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')

        slow_type(email_input, 'invalidemailformat')
        slow_type(password_input, '1234')

        time.sleep(1)
        delete_last_characters(email_input, 2)

        time.sleep(1)
        delete_last_characters(password_input, 1)

        time.sleep(2)

        email_error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Format Email tidak valid.')]")
        password_error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Password harus di antara 6 dan 30.')]")

        if email_error_message:
            print("Email format validation works: 'Format Email tidak valid.' message is displayed.")
        if password_error_message:
            print("Password length validation works: 'Password harus di antara 6 dan 30.' message is displayed.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(3)
        driver.quit()

validate_email_and_password()
