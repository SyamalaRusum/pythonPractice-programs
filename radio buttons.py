from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
radbtn=driver.find_element(By.XPATH,'//input[@value="radio1"]')
radbtn.click()
assert radbtn.is_selected()
