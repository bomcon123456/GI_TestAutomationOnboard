from selenium.common.exceptions import (NoSuchElementException, TimeoutException)


class BaseModal:
    def __init__(self, browser, modal_locator):
        self.browser = browser
        self.modal_locator = modal_locator
        self.close_button_locator = '.close'

    def is_visible(self):
        return self.browser.is_element_visible(self.modal_locator)

    def is_element_inside_clickable(self, timeout=10):
        try:
            self.browser.get_waited_clickable_element(self.close_button_locator, timeout)
        except (NoSuchElementException, TimeoutException):
            return False
        return True
