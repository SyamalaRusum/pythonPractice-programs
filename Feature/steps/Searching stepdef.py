from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")

driver=webdriver.Chrome()
@given("open the browser")
def step_impl(context):
    print("Browser name:",driver.name)

@when("load the url")
def step_impl(context):
    driver.get("https://www.google.com")

@then("search for (?P<item>.+)")
def step_impl(context, item):
    driver.find_element(By.ID,'APjFqb').send_keys(item)

@step("close the browser")
def step_impl(context):
    driver.close()


