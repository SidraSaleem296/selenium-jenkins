from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Path to the Chrome driver
service = Service("/usr/bin/chromium-driver")

# Set up the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the web app (Make sure it points to your Docker container's IP and port)
url = "http://44.244.209.87:8081"

try:
    # Open the webpage
    driver.get(url)

    # Check if the title contains the expected text
    assert "Sample Web App" in driver.title

    # Check if the button is present
    button = driver.find_element(By.ID, "submitBtn")
    assert button.is_displayed()

    # Click the button and wait for interaction (optional check)
    button.click()
    time.sleep(2)  # Wait for the action to complete

    print("Test passed!")
    
except Exception as e:
    print(f"Test failed: {str(e)}")
finally:
    driver.quit()  # Close the browser window
