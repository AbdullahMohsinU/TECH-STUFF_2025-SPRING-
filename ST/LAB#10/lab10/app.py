from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Load the HTML file
    driver.get("file:///C:/Users/cl2/PycharmProjects/pythonProject/log.html")

    # Wait for elements to be present
    wait = WebDriverWait(driver, 10)

    # Find and interact with the username field
    input_1 = wait.until(EC.presence_of_element_located((By.ID, "username")))
    input_1.send_keys("testuser")
    print("Username field displayed:", input_1.is_displayed())

    # Find and interact with the password field
    input_2 = wait.until(EC.presence_of_element_located((By.ID, "password")))
    input_2.send_keys("testpassword")
    print("Password field displayed:", input_2.is_displayed())

    # Find and click the login button
    button_login = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
    print("Login button enabled:", button_login.is_enabled())
    button_login.click()
    print("Login button clicked successfully")

    # Wait briefly to observe any post-submission changes
    time.sleep(2)

    # Optional: Check if elements are still present after click
    try:
        input_1 = wait.until(EC.presence_of_element_located((By.ID, "username")))
        print("Username field still present after click:", input_1.is_displayed())
    except (StaleElementReferenceException, TimeoutException):
        print("Username field not found after click, likely due to page change")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up
    driver.quit()