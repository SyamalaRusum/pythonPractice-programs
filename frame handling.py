from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe")    #switching to that frane
driver.find_element(By.XPATH,'//a[contains(@href,"sign_up")]')

driver.switch_to.default_content()
driver.find_element(By.XPATH,'//button[@class="btn btn-primary"]')
#raise an error bcoz it doesn't move to the main frame so, switch to default frame







