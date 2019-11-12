import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException, TimeoutException)


def setup_driver_environ():
    chrome_driver_dir = "libs/chromedriver"
    os.environ['webdriver.chrome.driver'] = chrome_driver_dir


def create_raw_driver():
    chrome_driver_dir = "libs/chromedriver"
    driver = webdriver.Chrome(chrome_driver_dir)
    # driver.maximize_window()
    # driver.implicitly_wait(2)
    return driver


class DriverWrapper:
    """
        Client class: Base class for all clients
        Since we want to use CSS Selectors, all the find will implicitly meaning find by css selectors
    """

    def __init__(self, url):
        self.driver = create_raw_driver()
        self.driver.get(url)
        self.main_window_handle = self.driver.current_window_handle

    def find_element(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def find_elements(self, locator):
        return self.driver.find_elements_by_css_selector(locator)

    def find_and_send_keys(self, locator, value):
        self.driver.find_element_by_css_selector(locator).send_keys(value)

    def get_waited_clickable_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def get_waited_visible_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def is_element_visible(self, locator, timeout=10):
        try:
            element = self.get_waited_visible_element(locator, timeout)
        except (NoSuchElementException, TimeoutException):
            return False
        return element.is_displayed()

    def switch_to_default(self):
        self.driver.switch_to.window(self.main_window_handle)

    def switch_to_window(self, url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url in self.driver.current_url:
                break

    def go_to_page(self, url):
        self.driver.get(url)
