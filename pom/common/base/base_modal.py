from selenium.common.exceptions import (NoSuchElementException, TimeoutException)
from selenium.webdriver.common.by import By


class BaseModal:
    modal_locator = None

    def __init__(self, browser):
        self.browser = browser
        self.close_button_locator = (By.CSS_SELECTOR, '.close')

    def is_presented(self):
        if self.modal_locator:
            return self.browser.is_element_visible(self.modal_locator)
        return None

    def is_element_inside_clickable(self, timeout=10):
        if self.modal_locator:
            try:
                self.browser.get_waited_clickable_element(self.close_button_locator, timeout)
            except (NoSuchElementException, TimeoutException):
                return False
            return True
        return False
