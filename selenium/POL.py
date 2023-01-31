import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# -- Chrome Browser \
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")

service_obj = Service("E:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://192.168.141.109:8004/")

print(driver.title)

time.sleep(5)
