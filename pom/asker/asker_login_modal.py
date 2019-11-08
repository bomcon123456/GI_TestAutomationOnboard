from pom.common.base.base_modal import BaseModal


class AskerLoginModal(BaseModal):
    # modal_id: 'modal-login'
    open_signup_locator = '.u-marginTop-3.u-textCenter.u-textGray.u-textSmall > a[role=\'button\']'

    def go_to_sign_up_modal(self):
        self.browser.get_waited_visible_element(self.open_signup_locator).click()
