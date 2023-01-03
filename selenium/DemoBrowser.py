from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# -- Chrome Browser \
#service_obj = Service("E:\chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

# -- Edge Browser
service_obj = Service("E:\edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
