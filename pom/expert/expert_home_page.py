from pom.common.base_page import BasePage


class ExpertHomepage(BasePage):
    intro_skip_button = 'button#js-introSkip'
    start_working_button = 'a[role=\'presentation\']'

    def start_working(self):
        self.browser.go_to_homepage()
        self.browser.get_waited_clickable_element(self.intro_skip_button).click()
        self.browser.get_waited_clickable_element(self.start_working_button).click()
