from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Automatically manage the chromedriver version
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def verify_title():
    driver.get("https://www.google.com")
    expected_title = "Google"
    actual_title = driver.title
    if actual_title == expected_title:
        print(f"Title verification successful! Actual title: '{actual_title}'")
    else:
        print(f"Title verification failed! Expected: '{expected_title}', Actual: '{actual_title}'")
    
    # Keep the browser open until user presses a key
    input("Press any key to close the browser...")  # The browser will remain open until you press a key
    
    driver.quit()

if __name__ == '__main__':
    verify_title()
