from selenium.common.exceptions import (NoSuchElementException, TimeoutException)

from pom.common.base.base_page import BasePage


class ExpertWorkPage(BasePage):
    waiting_question_locator = '.waiting-question'
    claim_button_locator = 'a#claim_button_locator-button'
    submit_button_locator = 'button#confirm-claim_button_locator-button'

    def click_claim_button(self):
        self.browser.get_waited_clickable_element(self.claim_button_locator).click()

    def click_submit_question(self):
        self.browser.get_waited_clickable_element(self.submit_button_locator).click()

    def is_loaded(self):
        return self.browser.is_element_visible(self.waiting_question_locator)

    def is_active(self):
        is_on_workspace_route = '/workspace' in self.browser.driver.current_url
        return is_on_workspace_route
