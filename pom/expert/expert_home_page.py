from .base_expert_page import BaseExpertPage


class ExpertHomepage(BaseExpertPage):
    intro_skip_button = 'button#js-introSkip'
    start_working_button = 'a[role=\'presentation\']'

    def start_working(self):
        self.expert.go_to_hompage()
        self.expert.get_waited_clickable_element(self.intro_skip_button).click()
        self.expert.get_waited_clickable_element(self.start_working_button).click()
