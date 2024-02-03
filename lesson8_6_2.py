import time

from selenium import webdriver

driver = webdriver.Chrome()

LINK = "https://demoqa.com/text-box"
NAME = "Test Testovich"
EMAIL = "test@co.com"
CURR_ADDRESS = "SPB"
PERM_ADDRESS = "MSC"


def test_name_field():
    driver.get(LINK)

    time.sleep(2)

    full_name_field = driver.find_element("xpath", "//input[@id='userName']")
    full_name_field.clear()
    assert full_name_field.get_attribute("value") == ""
    full_name_field.send_keys(NAME)
    assert full_name_field.get_attribute("value") == NAME

# email_field = driver.find_element("xpath", "//input[@id='userEmail']")
# email_field.clear()
# email_field.send_keys("test@co.com")
