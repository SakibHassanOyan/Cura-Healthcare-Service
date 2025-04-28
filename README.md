# Cura Healthcare Service - Web Automation Tests

## Project Description

This project contains automated tests for the Cura Healthcare Service website (https://katalon-demo-cura.herokuapp.com/). The tests are written using Selenium WebDriver with Python and unittest framework.  The primary goal of these tests is to verify the core functionalities of the website, including:

* Making an appointment
* Login with invalid credentials
* Verifying homepage elements
* Navigating to the history page

## Prerequisites

Before running these tests, ensure you have the following installed:

* **Python:** (Version 3.7 or later is recommended)
    * Check if you have Python installed:
        ```bash
        python --version
        ```
* **Selenium WebDriver:** You can install it using pip:
    ```bash
    pip install selenium
    ```
* **ChromeDriver:** Download the ChromeDriver that matches your Chrome browser version.  You can download it from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).  Make sure to add the ChromeDriver executable to your system's PATH.
* **Chrome Browser:** Ensure you have Google Chrome installed. The tests are configured to run on Chrome.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd CuraHealthcareService
    ```
    (Replace `<your_repository_url>` with the actual URL of your GitHub repository)

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    * On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    * On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```

4.  **Install the project dependencies (Selenium):**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: I assumed you have a `requirements.txt` file. If not, create one with `selenium` inside)*
    To create a requirements.txt file:
     ```bash
     pip freeze > requirements.txt
     ```

## How to Run the Tests

1.  **Navigate to the project directory:**
    ```bash
    cd CuraHealthcareService
    ```

2.  **Run all tests:**
    ```bash
    python cura_tests.py
    ```

3.  **Run a specific test:**
    ```bash
    python cura_tests.py -k test_successful_appointment_booking
    ```
    (Replace `test_successful_appointment_booking` with the name of the test you want to run)

## Test Execution Details

The test script (`cura_tests.py`) includes the following test cases:

* `test_successful_appointment_booking`: Verifies that a user can successfully book an appointment.
* `test_login_with_invalid_credentials`: Verifies the error message when a user tries to log in with invalid credentials.
* `test_verify_homepage_elements`: Verifies the presence and correctness of key elements on the homepage.
* `test_navigate_to_history_page`: Verifies that a user can navigate to the History page after logging in.

The script is configured to:

* Launch Chrome in guest mode to ensure a clean testing environment.
* Use explicit waits to handle dynamic elements and improve test reliability.
* Include `time.sleep()` calls for better visibility of the browser actions during test execution (these should be removed or reduced for production).
* Handle potential `TimeoutException` during the appointment confirmation step and prints the page source for debugging.

## Code Structure

* `cura_tests.py`: Contains the Selenium WebDriver tests using the unittest framework.
* `.venv/`: (Optional) Virtual environment directory.
* `requirements.txt`: Lists the project dependencies.

##  Further Improvements

* **Reporting:** Integrate a reporting library (e.g., HTMLTestRunner, Allure) for more detailed and visually appealing test reports.
* **Data-Driven Testing:** Parameterize the tests to run with multiple sets of data (e.g., different invalid login credentials, various appointment dates).
* **Continuous Integration (CI):** Set up CI (e.g., GitHub Actions) to automatically run the tests on every push or pull request.
* **Refactor Waits:** Refactor  `time.sleep()`  calls with more robust explicit waits.
* **Page Object Model:** Implement the Page Object Model design pattern to make the tests more maintainable and readable.

##  License

This project is licensed under the [Specify the license (e.g., MIT License)](LICENSE).

