from pom.common.base.base_page import BasePage


class ExpertHomepage(BasePage):
    # Locators for sign-up
    login_locator = '[role=\'button\']'
    open_signup_locator = '.dropdown strong'
    email_locator = 'input[name=\'email\']'
    password_locator = 'input[name=\'password\']'
    confirm_password_locator = 'input[name=\'confirmPassword\']'
    sign_up_button_locator = 'form > .btn.btn-block.btn-primary.m-t-10'
    # Locators for start working first time
    intro_skip_button_locator = 'button#js-introSkip'
    start_working_button_locator = 'a[role=\'presentation\']'

    def fill_email(self, email):
        self.browser.find_and_send_keys(self.email_locator, email)

    def fill_password(self, password):
        self.browser.find_and_send_keys(self.password_locator, password)

    def fill_confirm_password(self, password):
        self.browser.find_and_send_keys(self.confirm_password_locator, password)

    def click_login_button(self):
        self.browser.get_waited_visible_element(self.login_locator).click()

    def click_signup_link(self):
        self.browser.find_element(self.open_signup_locator).click()

    def click_signup_button(self):
        self.browser.get_waited_clickable_element(self.sign_up_button_locator).click()
        # after click next, will be redirected to 'https://expert-query.got-it.io/onboarding'

    def click_intro_skip_button(self):
        self.browser.get_waited_clickable_element(self.intro_skip_button_locator).click()

    def click_start_working_button(self):
        self.browser.get_waited_clickable_element(self.start_working_button_locator).click()

    def is_active(self):
        is_on_home_route = '/home' in self.browser.driver.current_url
        is_on_base_url = self.browser.driver.current_url == self.browser.base_url
        return is_on_base_url or is_on_home_route
