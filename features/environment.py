import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configReader


def before_scenario(context, driver):
    if configReader.readConfig("basic info", "browser") == "chrome":
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if configReader.readConfig("basic info", "browser") == "firefox":
        context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot'
                      , attachment_type=allure.attachment_type.PNG)
