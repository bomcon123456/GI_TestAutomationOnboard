from pom.common.base.base_modal import BaseModal


class AskerProblemExpertIntroModal(BaseModal):
    modal_locator = '#modal-problem-expert-intro'
    got_it_button_locator = '[class=\'gi-Button gi-Button--primary u-width-100\']'

    def click_gotit_button(self):
        self.browser.get_waited_visible_element(self.got_it_button_locator).click()
