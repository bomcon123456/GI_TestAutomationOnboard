from pom.common.base_page import BasePage


class AskerSignUp(BasePage):
    login_locator = '#test-login-button'
    open_signup_locator = '.u-marginTop-3.u-textCenter.u-textGray.u-textSmall > a[role=\'button\']'
    email_locator = 'div[role=\'document\'] input[name=\'email\']'
    password_locator = 'input[name=\'password\']'
    confirm_password_locator = 'input[name=\'confirmPassword\']'
    sign_up_button_locator = 'button#sign-up-button'
    next_button_locator = 'div[role=\'document\'] .gi-Button.gi-Button--accent.gi-Button--lg'

    def _wait_for_modal(self):
        self.browser.get_waited_visible_element('.close')

    def _open_sign_up_modal(self):
        self.browser.get_waited_visible_element(self.login_locator).click()
        self._wait_for_modal()
        self.browser.find_element(self.open_signup_locator).click()

    def _fill_sign_up_form(self, email, password):
        self._wait_for_modal()
        self.browser.find_and_send_keys(self.email_locator, email)
        self.browser.find_and_send_keys(self.password_locator, password)
        self.browser.find_and_send_keys(self.confirm_password_locator, password)

    def sign_up(self, email, password):
        self._open_sign_up_modal()
        self._fill_sign_up_form(email, password)
        self.browser.find_element(self.sign_up_button_locator).click()
        self.browser.get_waited_visible_element(self.next_button_locator).click()
