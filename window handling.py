from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.LINK_TEXT,'Open Tab').click()
print(driver.title)
tabvar=driver.window_handles
driver.switch_to.window(tabvar[1])
print(driver.title)
