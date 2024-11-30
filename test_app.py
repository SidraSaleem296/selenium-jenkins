import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WebAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_submit_form(self):
        driver = self.driver
        driver.get("http://44.243.227.79:5000")
        input_box = driver.find_element(By.NAME, "user_input")
        input_box.send_keys("Test Input")
        input_box.send_keys(Keys.RETURN)
        self.assertIn("You entered: Test Input", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
