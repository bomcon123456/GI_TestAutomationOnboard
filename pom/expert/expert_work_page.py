from pom.common.base.base_page import BasePage


class ExpertWorkPage(BasePage):
    claim_button_locator = 'a#claim_button_locator-button'
    submit_button_locator = 'button#confirm-claim_button_locator-button'

    def click_claim_button(self):
        self.browser.get_waited_clickable_element(self.claim_button_locator).click()

    def click_submit_question(self):
        self.browser.get_waited_clickable_element(self.submit_button_locator).click()
