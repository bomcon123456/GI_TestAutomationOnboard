from .client import Client


class Asker(Client):
    def __init__(self):
        super().__init__('https://asker-query.got-it.io/')

    def _wait_for_modal(self):
        self.get_waited_visible_element('.close')

    def _open_sign_up_modal(self, login_locator, open_sign_up_locator):
        self.get_waited_visible_element(login_locator).click()
        self._wait_for_modal()
        self.find_element(open_sign_up_locator).click()

    def _fill_sign_up_form(self, email, password, email_locator,
                           password_locator, confirm_password_locator):
        self._wait_for_modal()
        self.find_element(email_locator).send_keys(email)
        self.find_element(password_locator).send_keys(password)
        self.find_element(confirm_password_locator).send_keys(password)

    def sign_up(self, email, password, login_locator, open_sign_up_locator, email_locator,
                password_locator, confirm_password_locator,
                sign_up_locator, next_button_locator):
        self._open_sign_up_modal(login_locator, open_sign_up_locator)
        self._fill_sign_up_form(email, password, email_locator, password_locator, confirm_password_locator)
        self.find_element(sign_up_locator).click()
        self.get_waited_visible_element(next_button_locator).click()
