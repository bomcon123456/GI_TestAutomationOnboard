from pom.common.base.base_modal import BaseModal


class AskerLoginModal(BaseModal):
    open_signup_locator = '.u-marginTop-3.u-textCenter.u-textGray.u-textSmall > a[role=\'button\']'

    def __init__(self, browser):
        super().__init__(browser=browser, modal_locator='#modal-login')

    def click_signup_link(self):
        self.browser.get_waited_visible_element(self.open_signup_locator).click()
