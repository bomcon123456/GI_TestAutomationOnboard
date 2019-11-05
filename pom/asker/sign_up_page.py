from .base_asker_page import BaseAskerPage


class SignUp(BaseAskerPage):
    login_locator = '#test-login-button'
    open_signup_text = 'Sign up'
    email_field = 'div[role=\'document\'] input[name=\'email\']'
    password_field = 'input[name=\'password\']'
    confirm_password_field = 'input[name=\'confirmPassword\']'
    sign_up_button = 'button#sign-up-button'
    next_button = 'div[role=\'document\'] .gi-Button.gi-Button--accent.gi-Button--lg'

    def sign_up(self, email, password):
        self.asker.sign_up(email=email, password=password,
                           login_locator=self.login_locator, open_sign_up_text=self.open_signup_text,
                           email_locator=self.email_field,
                           password_locator=self.password_field, confirm_password_locator=self.confirm_password_field,
                           sign_up_locator=self.sign_up_button, next_button_locator=self.next_button)
