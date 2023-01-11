import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# -- Chrome Browser \
service_obj = Service("E:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windrowOpened = driver.window_handles
driver.switch_to.window(windrowOpened[1])
sentence = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
email = sentence.split(" ")
print(email)
print(email[4])
driver.switch_to.window(windrowOpened[0])
driver.find_element(By.ID, "username").send_keys(email[4])
driver.find_element(By.ID, "password").send_keys("learning")
dropdown = Select(driver.find_element(By.XPATH, "//select[@data-style='btn-info']"))
dropdown.select_by_value("teach")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(message)
# assert "Incorrect" in message


time.sleep(10)
