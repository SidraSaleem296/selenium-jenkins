from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode (without UI)

# Set up the WebDriver (Make sure you have chromedriver in your PATH)
driver = webdriver.Chrome(options=options)

def test_page_title():
    # Navigate to the deployed web app URL on the new port 8080
    driver.get("http://44.244.209.87:8080")  # Replace with your actual public IP and port
    
    # Test: Verify that the page title is correct
    assert driver.title == "Sample Web App", f"Expected title 'Sample Web App', but got {driver.title}"

def test_button_click():
    # Locate the button and click it
    button = driver.find_element(By.ID, "submitBtn")
    button.click()

    # Add a short wait to ensure the page reacts (if any)
    time.sleep(2)  # Adjust as needed for your app's behavior

    # Verify that the button was clicked (you can assert for any change in the UI here)
    assert button.is_displayed(), "Button not displayed after click."

if __name__ == "__main__":
    test_page_title()
    test_button_click()
    print("All tests passed!")

    driver.quit()
