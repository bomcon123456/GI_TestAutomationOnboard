import os
from selenium import webdriver


def setup_driver_environ():
    chrome_driver_dir = "libs/chromedriver"
    os.environ['webdriver.chrome.driver'] = chrome_driver_dir


def create_raw_driver():
    chrome_driver_dir = "libs/chromedriver"
    driver = webdriver.Chrome(chrome_driver_dir)
    driver.maximize_window()
    driver.implicitly_wait(2)
    return driver
