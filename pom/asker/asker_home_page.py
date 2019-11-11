from pom.common.base.base_page import BasePage


class AskerHomePage(BasePage):
    login_button_locator = '#test-login-button'
    question_field_locator = 'textarea[name=\'text\']'
    connect_now_for_free_button_locator = '.gi-Button.gi-Button--accent.gi-Button--lg.u-width-100'
    proceed_button_locator = '[class=\'gi-Button gi-Button--primary u-width-100\']'

    def click_connect_now_for_free_button(self):
        self.browser.get_waited_clickable_element(self.connect_now_for_free_button_locator).click()

    def click_got_it_proceed(self):
        self.browser.get_waited_clickable_element(self.proceed_button_locator).click()

    def click_login_button(self):
        self.browser.get_waited_clickable_element(self.login_button_locator).click()

    def fill_query_form(self):
        problem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                       'Donec bibendum, turpis dignissim lobortis dapibus, ' \
                       'libero arcu cursus elit, a luctus felis lacus et orci. ' \
                       'Aenean cursus, risus non sodales blandit, ' \
                       'dui nunc sagittis mi, ac gravida sapien magna at ipsum.'
        self.browser.get_waited_visible_element(self.question_field_locator).send_keys(problem_text)

    def is_active(self):
        is_on_home_route = '/home' in self.browser.driver.current_url
        is_on_base_url = self.browser.driver.current_url == self.browser.base_url
        return is_on_base_url or is_on_home_route
