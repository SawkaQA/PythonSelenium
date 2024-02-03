import time

from selenium import webdriver


driver = webdriver.Chrome()

LINK = "https://the-internet.herokuapp.com/status_codes"

driver.get(LINK)

buttons_links = driver.find_elements("xpath", "//ul/li/a")

for btn in buttons_links:
    btn.click()
    driver.back()

