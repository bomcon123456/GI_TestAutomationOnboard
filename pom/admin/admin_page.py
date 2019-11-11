import json

from dev_configs import (GMAIL_ACCOUNT, GMAIL_PASSWORD)
from pom.common.base.base_page import BasePage
from utils.bypass_onboard import bypass_onboard_expert


class AdminPage(BasePage):
    google_login_button_locator = '.btn.btn-google.btn-lg.btn-social'
    email_next_button_locator = '[jsname=\'k77Iif\'] .snByac'
    password_next_button_locator = '[jsname=\'k77Iif\'] .snByac'
    email_field_locator = '#identifierId'
    password_field_locator = 'input[name=\'password\']'
    user_panel_locator = '.dropdown > a'
    user_dropdown_locator = '.hi-menu  ul > li:nth-of-type(2) > a'
    first_expert_cell_locator = 'tr:nth-of-type(1) > td:nth-of-type(1) > a'

    def _deal_with_google_window(self):
        self.browser.switch_to_window(url='accounts.google')
        self.browser.get_waited_visible_element(self.email_field_locator).send_keys(GMAIL_ACCOUNT)
        self.browser.find_element(self.email_next_button_locator).click()
        self.browser.get_waited_visible_element(self.password_field_locator).send_keys(GMAIL_PASSWORD)
        self.browser.get_waited_clickable_element(self.password_next_button_locator).click()
        self.browser.switch_to_default()

    def _login(self):
        self.browser.get_waited_visible_element(self.google_login_button_locator).click()
        self._deal_with_google_window()

    def _get_newest_expert_id(self):
        self.browser.get_waited_clickable_element(self.user_panel_locator).click()
        self.browser.get_waited_visible_element(self.user_dropdown_locator).click()
        td = self.browser.get_waited_visible_element(self.first_expert_cell_locator)
        expert_id = td.text
        accesstoken_str = self.browser.driver.execute_script("return window.localStorage.getItem('accesstoken')")
        accesstoken_json = json.loads(accesstoken_str)
        access_token = accesstoken_json['access_token']
        return access_token, expert_id

    def login_and_approve_newest_expert(self):
        self._login()
        access_token, expert_id = self._get_newest_expert_id()
        bypass_onboard_expert(user_id=expert_id, access_token=access_token)
        self.browser.driver.quit()
