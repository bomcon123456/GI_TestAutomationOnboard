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

    def _open_sign_up_modal(self, login_locator, open_sign_up_locator):
        self.browser.get_waited_visible_element(login_locator).click()
        self._wait_for_modal()
        self.browser.find_element(open_sign_up_locator).click()

    def _fill_sign_up_form(self, email, password, email_locator,
                           password_locator, confirm_password_locator):
        self._wait_for_modal()
        self.browser.find_element(email_locator).send_keys(email)
        self.browser.find_element(password_locator).send_keys(password)
        self.browser.find_element(confirm_password_locator).send_keys(password)

    def sign_up(self, email, password):
        self._open_sign_up_modal(self.login_locator, self.open_signup_locator)
        self._fill_sign_up_form(email, password, self.email_locator, self.password_locator,
                                self.confirm_password_locator)
        self.browser.find_element(self.sign_up_button_locator).click()
        self.browser.get_waited_visible_element(self.next_button_locator).click()
