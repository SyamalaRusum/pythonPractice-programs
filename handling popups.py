from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID,"name").send_keys("HI")
driver.find_element(By.ID,"alertbtn").click()
alert=Alert(driver)
print(alert.text)
alert.accept()
#driver.find_element(By.ID,"confirmbtn").click()
#alert.dismiss()