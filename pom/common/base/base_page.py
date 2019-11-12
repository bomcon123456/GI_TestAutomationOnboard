class BasePage:
    url = None

    def __init__(self, browser):
        self.browser = browser

    def is_active(self):
        is_on_base_url = self.browser.driver.current_url == self.url
        return is_on_base_url
