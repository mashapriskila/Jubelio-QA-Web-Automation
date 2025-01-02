from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
email = os.getenv('JUBELIO_EMAIL')
password = os.getenv('JUBELIO_PASSWORD')

# Set up the WebDriver for Edge (make sure msedgedriver is in your PATH)
driver = webdriver.Edge()  # This will use EdgeDriver from the PATH

# Function to automate the login flow
def login_jubelio(username, password):
    try:
        # Navigate to the Jubelio login page
        driver.get('https://app2.jubelio.com/login')

        # Maximize the window
        driver.maximize_window()

        # Find and fill in the username and password fields
        driver.find_element(By.NAME, 'email').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)

        # Click the login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for the dashboard page to load by checking the URL
        time.sleep(10)  # You can also use WebDriver's explicit wait here

        # Check if redirected to the correct URL (home page)
        if driver.current_url == "https://app2.jubelio.com/home/getting-started":
            print("Login successful!")
        else:
            print("Login failed!")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Uncomment below line to close the browser after execution
    # driver.quit()

# Usage example
login_jubelio(email, password)
