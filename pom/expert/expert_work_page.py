from selenium.webdriver.common.by import By

from pom.common.base.base_page import BasePage


class ExpertWorkPage(BasePage):
    waiting_question_locator = (By.CSS_SELECTOR, '.waiting-question')
    claim_button_locator = (By.CSS_SELECTOR, '#claim-button')
    submit_button_locator = (By.CSS_SELECTOR, '#confirm-claim-button')
    click_to_diagnosis_button_locator = (By.CSS_SELECTOR, '.gi-ComposeInfo-changePhase > button')

    def click_claim_button(self):
        self.browser.get_waited_clickable_element(self.claim_button_locator).click()

    def click_submit_button(self):
        self.browser.get_waited_clickable_element(self.submit_button_locator).click()

    def is_loaded(self):
        return self.browser.is_element_visible(self.waiting_question_locator)

    def is_presented(self):
        is_on_workspace_route = '/workspace' in self.browser.driver.current_url
        return is_on_workspace_route

    def is_matched(self):
        return self.browser.is_element_visible(self.click_to_diagnosis_button_locator)
