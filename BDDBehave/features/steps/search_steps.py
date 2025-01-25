import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I navigate to google.com')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.google.com/")


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is:", title)
    assert "Googless" in title


@then(u'I enter the text as "{search_text}"')
def step_impl(context, search_text):
    context.driver.find_element(By.NAME, "q").send_keys(search_text)


@then(u'I click on search button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    btn = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    btn.click()
