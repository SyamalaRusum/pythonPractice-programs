from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#'dropdown-class-example'
drpdwn=Select(driver.find_element(By.NAME,'dropdown-class-example'))
drpdwn.select_by_visible_text("MBA")
drpdwn.select_by_value("option2")
drpdwn.select_by_index(2)