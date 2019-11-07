import json

from .base_admin_page import BaseAdminPage
from utils.bypass_onboard import bypass_onboard_expert
from configs import (GMAIL_ACCOUNT, GMAIL_PASSWORD)


class AdminLoginPage(BaseAdminPage):
    google_login_button = '.btn.btn-google.btn-lg.btn-social'
    email_next_button = '[jsname=\'k77Iif\'] .snByac'
    password_next_button = '[jsname=\'k77Iif\'] .snByac'
    email_field = '#identifierId'
    password_field = 'input[name=\'password\']'
    user_panel = '.dropdown > a'
    user_dropdown = '.hi-menu  ul > li:nth-of-type(2) > a'
    first_expert = 'tr:nth-of-type(1) > td:nth-of-type(1) > a'

    def _deal_with_google_window(self):
        self.client.switch_to_window(url='accounts.google')
        self.client.get_waited_visible_element(self.email_field).send_keys(GMAIL_ACCOUNT)
        self.client.find_element(self.email_next_button).click()
        self.client.get_waited_visible_element(self.password_field).send_keys(GMAIL_PASSWORD)
        self.client.get_waited_clickable_element(self.password_next_button).click()
        self.client.switch_to_default()

    def _login(self):
        self.client.get_waited_visible_element(self.google_login_button).click()
        self._deal_with_google_window()

    def _get_newest_expert_id(self):
        self.client.get_waited_clickable_element(self.user_panel).click()
        self.client.get_waited_visible_element(self.user_dropdown).click()
        td = self.client.get_waited_visible_element(self.first_expert)
        expert_id = td.text
        accesstoken_str = self.client.driver.execute_script("return window.localStorage.getItem('accesstoken')")
        accesstoken_json = json.loads(accesstoken_str)
        access_token = accesstoken_json['access_token']
        return access_token, expert_id

    def login_and_approve_newest_expert(self):
        self._login()
        access_token, expert_id = self._get_newest_expert_id()
        bypass_onboard_expert(user_id=expert_id, access_token=access_token)
        self.client.driver.quit()
