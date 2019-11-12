import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException, TimeoutException)


def setup_driver_environ():
    chrome_driver_dir = "libs/chromedriver"
    os.environ['webdriver.chrome.driver'] = chrome_driver_dir


def create_raw_driver(headless):
    chrome_driver_dir = "libs/chromedriver"
    if headless:
        options = Options()
        options.headless = True
        return webdriver.Chrome(chrome_driver_dir, chrome_options=options)
    return webdriver.Chrome(chrome_driver_dir)


class DriverWrapper:
    """
        Client class: Base class for all clients
        Since we want to use CSS Selectors, all the find will implicitly meaning find by css selectors
    """

    def __init__(self, url, headless=False):
        self.driver = create_raw_driver(headless)
        self.driver.get(url)
        self.main_window_handle = self.driver.current_window_handle

    def find_element(self, selector_locator):
        return self.driver.find_element(*selector_locator)

    def find_elements(self, selector_locator):
        return self.driver.find_elements(*selector_locator)

    def find_and_send_keys(self, selector_locator, value):
        self.driver.find_element(*selector_locator).send_keys(value)

    def get_waited_clickable_element(self, selector_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.element_to_be_clickable(selector_locator))

    def get_waited_visible_element(self, selector_locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.visibility_of_element_located(selector_locator))

    def is_element_visible(self, selector_locator, timeout=10):
        try:
            element = self.get_waited_visible_element(selector_locator, timeout)
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
