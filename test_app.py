from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_title():
    driver = webdriver.Chrome()
    driver.get("http://44.244.121.50:5000")
    assert "Simple Web App" in driver.title
    driver.quit()

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("http://44.244.121.50:5000")
    input_box = driver.find_element(By.NAME, "user_input")
    input_box.send_keys("Test Input")
    input_box.send_keys(Keys.RETURN)
    assert "You entered: Test Input" in driver.page_source
    driver.quit()
