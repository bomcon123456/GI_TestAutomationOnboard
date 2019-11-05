import time

from .base_asker_page import BaseAskerPage


class AskerHomePage(BaseAskerPage):
    query_field = 'textarea[name=\'text\']'
    start_query_button = '.gi-Button.gi-Button--accent.gi-Button--lg.u-width-100'

    def test(self):
        login_locator = '#test-login-button'
        user = 'input[name=\'email\']'
        password = 'input[name=\'password\']'
        login_button = 'button#login-button'
        self.asker.find_element(login_locator).click()
        time.sleep(1)
        self.asker.find_element(user).send_keys('askerSelenium2@gmail.com')
        self.asker.find_element(password).send_keys('MotConVit123!@')
        self.asker.find_element(login_button).click()
        self.query()

    def query(self):
        problem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                       'Donec bibendum, turpis dignissim lobortis dapibus, ' \
                       'libero arcu cursus elit, a luctus felis lacus et orci. ' \
                       'Aenean cursus, risus non sodales blandit, ' \
                       'dui nunc sagittis mi, ac gravida sapien magna at ipsum.'
        # Ask Max how to solve this without sleeping
        time.sleep(2)
        self.asker.find_element(self.query_field).send_keys(problem_text)
        self.asker.find_element(self.start_query_button).click()
