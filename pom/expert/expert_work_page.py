from .base_expert_page import BaseExpertPage


class ExpertWorkPage(BaseExpertPage):
    claim = 'a#claim-button'
    submit = 'button#confirm-claim-button'

    def claim_question(self):
        self.browser.get_waited_clickable_element(self.claim).click()
        self.browser.get_waited_clickable_element(self.submit).click()
