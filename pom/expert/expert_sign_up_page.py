from .base_expert_page import BaseExpertPage


class ExpertSignUp(BaseExpertPage):
    login_locator = '[role=\'button\']'
    open_signup_locator = '.dropdown strong'
    email_locator = 'input[name=\'email\']'
    password_locator = 'input[name=\'password\']'
    confirm_password_locator = 'input[name=\'confirmPassword\']'
    sign_up_button_locator = 'form > .btn.btn-block.btn-primary.m-t-10'
    next_button_locator = '.btn.btn-block.btn-warning.gi-popupControl--Right'

    def _open_sign_up_modal(self, login_locator, open_sign_up_locator):
        self.browser.get_waited_visible_element(login_locator).click()
        self.browser.find_element(open_sign_up_locator).click()

    def _fill_sign_up_form(self, email, password, email_locator,
                           password_locator, confirm_password_locator):
        self.browser.find_element(email_locator).send_keys(email)
        self.browser.find_element(password_locator).send_keys(password)
        self.browser.find_element(confirm_password_locator).send_keys(password)

    def sign_up(self, email, password):
        self._open_sign_up_modal(self.login_locator, self.open_signup_locator)
        self._fill_sign_up_form(email, password, self.email_locator, self.password_locator,
                                self.confirm_password_locator)
        self.browser.get_waited_clickable_element(self.sign_up_button_locator).click()
        self.browser.get_waited_visible_element(self.next_button_locator).click()
