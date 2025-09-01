from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
time.sleep(2)
expected_title = "Google"
expected_url = "https://www.google.com"
actual_url = driver.current_url
if actual_url.startswith(expected_url):
    print(" Test Case 2 Passed: URL is correct.")
else:
    print(f" Test Case 2 Failed: Expected URL starting with '{expected_url}', but got '{actual_url}'.")
driver.quit()
