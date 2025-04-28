from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from datetime import date, timedelta
from selenium.common.exceptions import TimeoutException
import time  # Import the time module

class CuraDemoTests(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--guest")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://katalon-demo-cura.herokuapp.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_successful_appointment_booking(self):
        # Click Make Appointment
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        time.sleep(1)  # Wait for 1 second

        # Login
        self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        self.driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(1)  # Wait for 1 second

        # Wait for an element on the logged-in page
        self.wait.until(EC.presence_of_element_located((By.ID, "combo_facility")))

        # Book Appointment
        self.wait.until(EC.presence_of_element_located((By.ID, "combo_facility"))).click()
        self.driver.find_element(By.XPATH, "//option[@value='Hongkong CURA Healthcare Center']").click()
        self.driver.find_element(By.ID, "chk_hospotal_readmission").click()
        self.driver.find_element(By.ID, "radio_program_medicare").click()

        # Select date
        today = date.today()
        future_date = today + timedelta(days=5)
        date_str = future_date.strftime("%d/%m/%Y")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#txt_visit_date + .input-group-addon"))).click()
        self.driver.find_element(By.ID, "txt_visit_date").send_keys(date_str)
        self.driver.find_element(By.ID, "txt_visit_date").send_keys(Keys.TAB)
        time.sleep(0.5)  # Short wait after date selection

        self.wait.until(EC.element_to_be_clickable((By.ID, "txt_comment"))).send_keys("This is a test appointment.")
        time.sleep(0.5)  # Short wait before booking

        # Explicit wait and click Book Appointment
        book_appointment_button = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-book-appointment")))
        book_appointment_button.click()
        time.sleep(2)  # Wait to see the confirmation page

        # Assertion
        try:
            confirmation_text = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Appointment Confirmation']"))).text
            self.assertEqual(confirmation_text, "Appointment Confirmation", "Appointment booking failed.")
        except TimeoutException:
            print("Timeout occurred while waiting for Appointment Confirmation. Current page source:")
            print(self.driver.page_source)
            raise

    def test_login_with_invalid_credentials(self):
        # Click Make Appointment
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        time.sleep(1)

        # Attempt login with invalid credentials
        self.driver.find_element(By.ID, "txt-username").send_keys("invalid_user")
        self.driver.find_element(By.ID, "txt-password").send_keys("invalid_password")
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(1)

        # Assertion
        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-danger"))).text
        self.assertEqual(error_message, "Login failed! Please ensure the username and password are valid.", "Login with invalid credentials did not show error.")

    def test_verify_homepage_elements(self):
        # Assertion for title
        self.assertEqual(self.driver.title, "CURA Healthcare Service", "Incorrect page title.")
        time.sleep(0.5)

        # Assertion for heading
        heading = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'CURA Healthcare')]"))).text
        self.assertEqual(heading, "CURA Healthcare Service", "Homepage heading is incorrect.")
        time.sleep(0.5)

        # Assertion for Make Appointment button
        make_appointment_button = self.wait.until(EC.presence_of_element_located((By.ID, "btn-make-appointment")))
        self.assertTrue(make_appointment_button.is_displayed(), "'Make Appointment' button is not visible.")
        time.sleep(0.5)

    def test_navigate_to_history_page(self):
        # Click Make Appointment to navigate to the login page (where the menu is visible after login)
        self.driver.find_element(By.ID, "btn-make-appointment").click()
        time.sleep(1)

        # Login
        self.driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        self.driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        self.driver.find_element(By.ID, "btn-login").click()
        time.sleep(1)

        # Wait for an element on the logged-in page to ensure login is complete
        self.wait.until(EC.presence_of_element_located((By.ID, "combo_facility")))

        # Click the toggle button to open the menu
        toggle_button = self.wait.until(EC.presence_of_element_located((By.ID, "menu-toggle")))
        toggle_button.click()
        time.sleep(0.5)

        # Now, navigate to History page
        history_link_xpath = "//a[@href='history.php#history']"
        history_link = self.wait.until(EC.presence_of_element_located((By.XPATH, history_link_xpath)))
        history_link.click()
        time.sleep(1)

        # Assertion
        history_heading = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='History']"))).text
        self.assertEqual(history_heading, "History", "Navigation to History page failed.")
        time.sleep(0.5)

if __name__ == '__main__':
    unittest.main()