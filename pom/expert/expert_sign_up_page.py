from pom.common.base_page import BasePage


class ExpertSignUp(BasePage):
    login_locator = '[role=\'button\']'
    open_signup_locator = '.dropdown strong'
    email_locator = 'input[name=\'email\']'
    password_locator = 'input[name=\'password\']'
    confirm_password_locator = 'input[name=\'confirmPassword\']'
    sign_up_button_locator = 'form > .btn.btn-block.btn-primary.m-t-10'
    next_button_locator = '.btn.btn-block.btn-warning.gi-popupControl--Right'

    def _open_sign_up_modal(self):
        self.browser.get_waited_visible_element(self.login_locator).click()
        self.browser.find_element(self.open_signup_locator).click()

    def _fill_sign_up_form(self, email, password):
        self.browser.find_and_send_keys(self.email_locator, email)
        self.browser.find_and_send_keys(self.password_locator, password)
        self.browser.find_and_send_keys(self.confirm_password_locator, password)

    def sign_up(self, email, password):
        self._open_sign_up_modal()
        self._fill_sign_up_form(email, password)
        self.browser.get_waited_clickable_element(self.sign_up_button_locator).click()
        self.browser.get_waited_visible_element(self.next_button_locator).click()
