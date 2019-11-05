from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from utils.drivers import create_raw_driver


class Client:
    """
        Client class: Base class for all clients
        Since we want to use CSS Selectors, all the find will implicitly meaning find by css selectors
    """

    def __init__(self, base_url):
        self.driver = create_raw_driver()
        self.base_url = base_url
        self.driver.get(base_url)
        self.main_window_handle = self.driver.current_window_handle

    def find_element(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def find_elements(self, locator):
        return self.driver.find_elements_by_css_selector(locator)

    def wait_until_invisible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, locator)))

    def get_waited_clickable_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def get_waited_visible_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url in self.driver.current_url:
                break