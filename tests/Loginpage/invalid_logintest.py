from selenium import webdriver
from selenium.webdriver.common.by import By
import time

email = 'emailsalah@gmail.com'
password = 123456

driver = webdriver.Edge()  

def login_jubelio(username, password):
    try:
        # Navigate to the Jubelio login page
        driver.get('https://app2.jubelio.com/login')
        driver.maximize_window()

        # Fill in email and password fields
        driver.find_element(By.NAME, 'email').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)

        # Click the submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Allow time for page load
        time.sleep(3)

        try:
            # Find the <li> element that contains the text 'Password atau email anda salah'
            error_message_element = driver.find_element(By.XPATH, "//li[contains(text(), 'Password atau email anda salah')]")

            if error_message_element:
                print("Element found: ", error_message_element.text)

        except Exception as e:
            print(f"Error message element not found or an error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

login_jubelio(email, password)
