from pom.common.base.base_modal import BaseModal


class AskerSignupModal(BaseModal):
    email_locator = 'div[role=\'document\'] input[name=\'email\']'
    password_locator = 'input[name=\'password\']'
    confirm_password_locator = 'input[name=\'confirmPassword\']'
    sign_up_button_locator = 'button#sign-up-button'
    next_button_locator = 'div[role=\'document\'] .gi-Button.gi-Button--accent.gi-Button--lg'

    def __init__(self, browser):
        super().__init__(browser=browser, modal_locator='#modal-signup')

    def fill_email(self, email):
        self.browser.find_and_send_keys(self.email_locator, email)

    def fill_password(self, password):
        self.browser.find_and_send_keys(self.password_locator, password)

    def fill_confirm_password(self, password):
        self.browser.find_and_send_keys(self.confirm_password_locator, password)

    def click_signup_button(self):
        self.browser.find_element(self.sign_up_button_locator).click()
