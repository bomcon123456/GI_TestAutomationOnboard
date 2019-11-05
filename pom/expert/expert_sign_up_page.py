from .base_expert_page import BaseExpertPage


class ExpertSignUp(BaseExpertPage):
    login_locator = '[role=\'button\']'
    open_signup = '.dropdown strong'
    email_field = 'input[name=\'email\']'
    password_field = 'input[name=\'password\']'
    confirm_password_field = 'input[name=\'confirmPassword\']'
    sign_up_button = 'form > .btn.btn-block.btn-primary.m-t-10'
    next_button = '.btn.btn-block.btn-warning.gi-popupControl--Right'

    def sign_up(self, email, password):
        self.expert.sign_up(email=email, password=password,
                            login_locator=self.login_locator, open_sign_up_locator=self.open_signup,
                            email_locator=self.email_field,
                            password_locator=self.password_field, confirm_password_locator=self.confirm_password_field,
                            sign_up_locator=self.sign_up_button, next_button_locator=self.next_button)
