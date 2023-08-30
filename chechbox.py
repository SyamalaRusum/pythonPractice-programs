from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#checkboxes=driver.find_element(By.XPATH,'//input[@type="checkbox"]')
op2=driver.find_element(By.ID,'checkBoxOption2')
op2.click()
assert op2.is_selected()