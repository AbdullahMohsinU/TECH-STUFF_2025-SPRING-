from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
html_path = r"file:///C:/Users/23fa-048-st/Desktop/lab8/index.html"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(html_path)
time.sleep(2)
css1 = driver.find_element(By.CSS_SELECTOR, "input.btn[value='Submit']")
css2 = driver.find_element(By.CSS_SELECTOR, "input.btn[value='Reset']")
link1 = driver.find_element(By.LINK_TEXT, "About Us")    # assuming these links exist, add in your html if needed
link2 = driver.find_element(By.LINK_TEXT, "Contact")
xpath1 = driver.find_element(By.XPATH, "//label[text()='Username:']")
xpath2 = driver.find_element(By.XPATH, "//label[text()='Password:']")
id1 = driver.find_element(By.ID, "username")
id2 = driver.find_element(By.ID, "password")
name1 = driver.find_element(By.NAME, "email")
name2 = driver.find_element(By.NAME, "phone")
print("Found all 10 elements successfully.")
id1.send_keys("labuser")
id2.send_keys("pass123")
name1.send_keys("lab@example.com")
name2.send_keys("1234567890")
css1.click()
driver.quit()
