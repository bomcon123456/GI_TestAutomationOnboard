from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pom.common.base.base_modal import BaseModal


class TermsConditionsModal(BaseModal):
    # modal_id: 'modal-terms-and-conditions'
    next_button_xpath_locator = '//div[@id=\'modal-terms-and-conditions\']//button[contains(text(),\'NEXT\')]'

    def click_next_button(self, timeout=10):
        wait = WebDriverWait(self.browser.driver, timeout)
        by_next_button = wait.until(
            expected_conditions.invisibility_of_element_located((By.XPATH, self.next_button_xpath_locator)))
        by_next_button.click()
