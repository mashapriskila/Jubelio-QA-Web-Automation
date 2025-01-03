# Jubelio QA Web Automation

This repository contains web automation scripts for Jubelio using Selenium and Python. It automates the testing of the Jubelio web application, focusing on various scenarios like login, inventory page actions, and form validation.

## Getting Started

Follow the instructions below to set up the project and run the tests.

### 1. Clone the Project

Clone this repository to your local machine using the following command:

git clone https://github.com/mashapriskila/Jubelio-QA-Web-Automation.git

### 2. Set Up the .env File

After cloning the project, create a `.env` file in the root directory of the project.

This `.env` file should contain your registered Jubelio email and password in the following format:

JUBELIO_EMAIL=your-email@example.com
JUBELIO_PASSWORD=your-password

Make sure the email and password correspond to the credentials you use to log in to the Jubelio web application (https://app2.jubelio.com/login).

### 3. Install WebDriver
To run the tests, you will need a WebDriver for your browser. In this project, EdgeDriver is used by default for Microsoft Edge. You can download it from here (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?cs=2650699278&form=MA13LH)

Once downloaded, ensure the WebDriver is added to your system's PATH environment variable. This allows the project to use it automatically.

If you prefer to use a different WebDriver, such as ChromeDriver, you can replace the EdgeDriver path in the code with the correct path for your chosen WebDriver.

### 4. Install Dependencies
Before running the tests, you'll need to install the necessary dependencies.

The project uses the following libraries:

1. Python: The programming language used for this project.
2. Selenium: For automating web testing.
3. pytest: For running tests in Visual Studio Code or the command line.
4. python-dotenv: For loading environment variables from the .env file

### 5. Running the Tests
Once you have completed the setup, you can run the tests to verify everything is working correctly.

To run a specific test file, use the following command:

python -m pytest tests/Inventorypage/notcompleteform_item.py -s

Make sure to adjust the command according to the path of the test file you want to run. For example, if you're testing another file, replace tests/Inventorypage/notcompleteform_item.py with the appropriate path.

### 6. Project Structure
The project contains test files for different parts of the Jubelio web application, including:

Login validation
Inventory page 

Each test file automates a specific scenario and uses the Selenium WebDriver to interact with the Jubelio web application.

### 7. Customizing the Tests
You can modify the test scripts or add new ones based on your needs. The tests are structured in a way that you can easily customize the input data, WebDriver settings, or any other part of the script.

Make sure to use the correct locators (XPath, class name, etc.) if there are changes to the Jubelio web application's UI.

### 8. Troubleshooting
If you encounter any errors related to the WebDriver, ensure that the driver is properly installed and added to your system’s PATH.
If the test results are not as expected, verify that the credentials in the .env file are correct and that you're accessing the correct URLs in the tests.

