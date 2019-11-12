from behave import *

from dev_configs import (ASKER_EMAIL_PREFIX, EXPERT_EMAIL_PREFIX, PASSWORD_COMMON)
from pom.admin.admin_page import AdminPage
from pom.asker.asker_home_page import AskerHomePage
from pom.asker.asker_login_modal import AskerLoginModal
from pom.asker.asker_signup_modal import AskerSignupModal
from pom.asker.asker_problem_expert_intro_modal import AskerProblemExpertIntroModal
from pom.asker.asker_problem_page import AskerProblemPage
from pom.common.terms_conditions_modal import TermsConditionsModal
from pom.expert.expert_home_page import ExpertHomepage
from pom.expert.expert_work_page import ExpertWorkPage
from utils.email_gen import generate_email

use_step_matcher("re")


@given("I'm on Asker Home Page")
def step_impl(context):
    asker_homepage = AskerHomePage(context.asker)
    assert asker_homepage.is_active()
    context.asker_homepage = asker_homepage


@when("I open Asker SignUp Modal")
def step_impl(context):
    context.asker_homepage.click_login_button()
    asker_login_modal = AskerLoginModal(context.asker)
    assert asker_login_modal.is_visible()
    assert asker_login_modal.is_element_inside_clickable()
    asker_login_modal.click_signup_link()
    asker_signup_modal = AskerSignupModal(context.asker)
    assert asker_signup_modal.is_visible()
    context.asker_signup_modal = asker_signup_modal


@step("I enter email")
def step_impl(context):
    email = generate_email(ASKER_EMAIL_PREFIX)
    context.asker_signup_modal.fill_email(email)


@step("I enter password")
def step_impl(context):
    context.asker_signup_modal.fill_password(PASSWORD_COMMON)


@step("I enter confirm password")
def step_impl(context):
    context.asker_signup_modal.fill_confirm_password(PASSWORD_COMMON)


@step("I press sign up")
def step_impl(context):
    context.asker_signup_modal.click_signup_button()


@then("Asker's Terms Conditions Modal should be presented")
def step_impl(context):
    asker_terms_and_conditions_modal = TermsConditionsModal(context.asker)
    assert asker_terms_and_conditions_modal.is_visible()
    context.asker_terms_and_conditions_modal = asker_terms_and_conditions_modal


@when("I press Next")
def step_impl(context):
    assert context.asker_terms_and_conditions_modal.is_element_inside_clickable()
    context.asker_terms_and_conditions_modal.click_next_button()


@then("I should be redirected to Asker Home Page")
def step_impl(context):
    assert context.asker_homepage.is_active()


@when("Expert is on Expert Home Page")
def step_impl(context):
    expert_homepage = ExpertHomepage(context.expert)
    assert expert_homepage.is_active()
    context.expert_homepage = expert_homepage


@step("Expert open Signup Dropdown")
def step_impl(context):
    context.expert_homepage.click_login_button()
    context.expert_homepage.click_signup_link()


@when("Expert enters email")
def step_impl(context):
    expert_email = generate_email(EXPERT_EMAIL_PREFIX)
    context.expert_homepage.fill_email(expert_email)


@step("Expert enters password")
def step_impl(context):
    context.expert_homepage.fill_password(PASSWORD_COMMON)


@step("Expert enters confirm password")
def step_impl(context):
    context.expert_homepage.fill_confirm_password(PASSWORD_COMMON)


@step("Expert click Sign Up button")
def step_impl(context):
    context.expert_homepage.click_signup_button()


@then("Expert's Terms Conditions Modal should be presented")
def step_impl(context):
    expert_terms_and_conditions_modal = TermsConditionsModal(context.expert)
    assert expert_terms_and_conditions_modal.is_visible()
    context.expert_terms_and_conditions_modal = expert_terms_and_conditions_modal


@when("Expert presses Next")
def step_impl(context):
    context.expert_terms_and_conditions_modal.click_next_button()


@then("Expert should be redirected to Expert Onboard Page")
def step_impl(context):
    assert context.expert_homepage.is_active()


@when("Admin bypass that expert")
def step_impl(context):
    admin_page = AdminPage(context.admin)
    admin_page.login_and_approve_newest_expert()


@step("Expert go to Expert Home Page")
def step_impl(context):
    context.expert.go_to_page('https://expert-query.got-it.io/')
    assert context.expert_homepage.is_active()


@step("Expert press Start Working Button")
def step_impl(context):
    context.expert_homepage.click_intro_skip_button()
    context.expert_homepage.click_start_working_button()


@then("Expert should see the Expert Workspace Page")
def step_impl(context):
    expert_workspace_page = ExpertWorkPage(context.expert)
    assert expert_workspace_page.is_loaded()
    assert expert_workspace_page.is_active()
    context.expert_workspace_page = expert_workspace_page


@when("I post a question")
def step_impl(context):
    context.asker_homepage.fill_query_form()
    context.asker_homepage.click_connect_now_for_free_button()


@when("Expert claims the question")
def step_impl(context):
    context.expert_workspace_page.click_claim_button()
    context.expert_workspace_page.click_submit_button()


@then("I should see Problem Expert Intro Modal")
def step_impl(context):
    asker_problem_expert_intro = AskerProblemExpertIntroModal(context.asker)
    context.asker_problem_expert_intro = asker_problem_expert_intro


@when("I press GotIt button")
def step_impl(context):
    if context.asker_problem_expert_intro.is_visible():
        context.asker_problem_expert_intro.click_gotit_button()


@then("I should be in the same room with that expert")
def step_impl(context):
    asker_problem_page = AskerProblemPage(context.asker)
    assert asker_problem_page.is_active()
    assert context.expert_workspace_page.is_matched()
