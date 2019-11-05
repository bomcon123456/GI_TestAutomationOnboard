from .base_asker_page import BaseAskerPage


class AskerSignUp(BaseAskerPage):
    login_locator = '#test-login-button'
    open_signup = '.u-marginTop-3.u-textCenter.u-textGray.u-textSmall > a[role=\'button\']'
    email_field = 'div[role=\'document\'] input[name=\'email\']'
    password_field = 'input[name=\'password\']'
    confirm_password_field = 'input[name=\'confirmPassword\']'
    sign_up_button = 'button#sign-up-button'
    next_button = 'div[role=\'document\'] .gi-Button.gi-Button--accent.gi-Button--lg'

    def sign_up(self, email, password):
        self.asker.sign_up(email=email, password=password,
                           login_locator=self.login_locator, open_sign_up_locator=self.open_signup,
                           email_locator=self.email_field,
                           password_locator=self.password_field, confirm_password_locator=self.confirm_password_field,
                           sign_up_locator=self.sign_up_button, next_button_locator=self.next_button)
