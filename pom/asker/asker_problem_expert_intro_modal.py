from pom.common.base.base_modal import BaseModal


class AskerProblemExpertIntroModal(BaseModal):
    got_it_button_locator = '[class=\'gi-Button gi-Button--primary u-width-100\']'

    def __init__(self, browser):
        super().__init__(browser=browser, modal_locator='#modal-problem-expert-intro')

    def click_gotit_button(self):
        self.browser.get_waited_visible_element(self.got_it_button_locator).click()
