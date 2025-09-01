from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
email = "testuser1234@example.com"
password = "Test@1234"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
try:
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    dashboard = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-title span.base"))
    )
    print("✅ Login Test Passed: Logged in as", dashboard.text)
except Exception as e:
    driver.save_screenshot("login_failed.png")
    print("❌ Login Test Failed:", e)
time.sleep(3)
driver.quit()
