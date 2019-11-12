from selenium.webdriver.common.by import By

from pom.common.base.base_modal import BaseModal


class AskerProblemExpertIntroModal(BaseModal):
    modal_locator = (By.CSS_SELECTOR, '#modal-problem-expert-intro')
    got_it_button_locator = (By.CSS_SELECTOR, '[class=\'gi-Button gi-Button--primary u-width-100\']')

    def click_gotit_button(self):
        self.browser.get_waited_visible_element(self.got_it_button_locator).click()
