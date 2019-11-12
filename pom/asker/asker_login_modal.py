from selenium.webdriver.common.by import By

from pom.common.base.base_modal import BaseModal


class AskerLoginModal(BaseModal):
    modal_locator = (By.CSS_SELECTOR, '#modal-login')
    open_signup_locator = (By.CSS_SELECTOR, '.u-marginTop-3.u-textCenter.u-textGray.u-textSmall > a[role=\'button\']')

    def click_signup_link(self):
        self.browser.get_waited_visible_element(self.open_signup_locator).click()
