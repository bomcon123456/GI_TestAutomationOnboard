import time

from pom.common.base_page import BasePage


class AskerHomePage(BasePage):
    query_field = 'textarea[name=\'text\']'
    start_query_button = '.gi-Button.gi-Button--accent.gi-Button--lg.u-width-100'

    def login_and_query(self):
        login_locator = '#test-login-button'
        user = 'input[name=\'email\']'
        password = 'input[name=\'password\']'
        login_button = 'button#login-button'
        self.browser.find_element(login_locator).click()
        time.sleep(1)
        self.browser.find_element(user).send_keys('askerSelenium2@gmail.com')
        self.browser.find_element(password).send_keys('MotConVit123!@')
        self.browser.find_element(login_button).click()
        self.query()

    def query(self):
        problem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                       'Donec bibendum, turpis dignissim lobortis dapibus, ' \
                       'libero arcu cursus elit, a luctus felis lacus et orci. ' \
                       'Aenean cursus, risus non sodales blandit, ' \
                       'dui nunc sagittis mi, ac gravida sapien magna at ipsum.'
        self.browser.get_waited_visible_element(self.query_field).send_keys(problem_text)
        self.browser.get_waited_clickable_element(self.start_query_button).click()
