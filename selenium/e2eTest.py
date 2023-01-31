import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# -- Chrome Browser \
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")

service_obj = Service("E:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")

for product in products:
    product_name = product.find_element(By.CSS_SELECTOR, "div h4 a").text
    if product_name == "Blackberry":
        product.find_element(By.CSS_SELECTOR, "div button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
success_text = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
print(success_text)

assert "Success! Thank you!" in success_text

time.sleep(10)
