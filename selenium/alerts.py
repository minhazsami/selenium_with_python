import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# -- Chrome Browser \
service_obj = Service("E:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
name = "Minhaz"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()


time.sleep(10)
