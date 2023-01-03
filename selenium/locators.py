from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome Browser \
service_obj = Service("E:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSS sector, ClassName, Name, LinkText
driver.find_element(By.NAME, "email").send_keys("minhaz@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# //tagname[@attribute='value'] - Xpath selector syntax
# tagname[attribute='value'] - CSS sector syntax
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Mohammed Minhaz")
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
