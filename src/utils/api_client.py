from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def bypass_payment_check(platform_url, login_url, email, password):
    """Automate login and bypass payment check."""
    # Set up Selenium WebDriver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to login page
        print(f"Navigating to {login_url}...")
        driver.get(login_url)
        time.sleep(3)  # Wait for the page to load

        # Locate and fill email and password fields
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys(email)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # wait for the page to load
        try:
            WebDriverWait(driver, 10).until(
                lambda d: d.current_url.startswith(platform_url)
            )
        except TimeoutException:
            print("Login failed or dashboard did not load in time.")
            return None

        print(f"Login successful! Current URL: {driver.current_url}")

        # Check for payment modal (if applicable)
        try:
            payment_modal_close_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "payment-modal-close"))
            )
            payment_modal_close_button.click()
            print("Payment check bypassed!")
        except TimeoutException:
            print("No payment modal found.")

        # Collect session data (customize based on your application)
        session_data = {
            "cookies": driver.get_cookies(),
            "session_url": driver.current_url,
        }
        return session_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        driver.quit()