from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from dotenv import load_dotenv
import os

email = 'emailsalah@gmail.com'
password = 123456

driver = webdriver.Edge()  

def login_jubelio(username, password):
    try:
        # Navigate to the Jubelio login page
        driver.get('https://app2.jubelio.com/login')

       
        driver.maximize_window()

        
        driver.find_element(By.NAME, 'email').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)

        #
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        
        time.sleep(3) 

        try:
          element = driver.find_element(By.TAG_NAME, 'li')  

    
          print("Element found: ", element.text)

        except Exception as e:
           print(f"An error occurred: {e}")


    except Exception as e:
        print(f"An error occurred: {e}")

    

login_jubelio(email, password)
