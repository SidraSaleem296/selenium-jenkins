from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (without UI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver (Make sure you have chromedriver installed)
driver = webdriver.Chrome(options=options)

def test_page_title():
    print("Testing page title...")
    driver.get("http://44.244.209.87:5001")  # Update with your public IP and port
    
    # Test: Verify that the page title is correct
    assert driver.title == "Sample Web App", f"Expected title 'Sample Web App', but got {driver.title}"

def test_button_click():
    print("Testing button click...")
    button = driver.find_element(By.ID, "submitBtn")  # Change the ID based on your HTML
    button.click()
    
    # Add a short wait to ensure the page reacts
    time.sleep(2)

    # Check if the button is still displayed (or other logic after clicking)
    assert button.is_displayed(), "Button not displayed after click."

if __name__ == "__main__":
    test_page_title()
    test_button_click()
    print("All tests passed!")

    driver.quit()
