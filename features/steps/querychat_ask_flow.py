import time

from behave import *

from dev_configs import (ASKER_EMAIL_PREFIX, EXPERT_EMAIL_PREFIX, PASSWORD_COMMON)
from pom.asker.asker_home_page import AskerHomePage
from pom.asker.asker_login_modal import AskerLoginModal
from pom.asker.asker_signup_modal import AskerSignupModal
from pom.common.terms_conditions_modal import TermsConditionsModal
from utils.email_gen import generate_email

use_step_matcher("re")


@given("I'm on AskerHomePage")
def step_impl(context):
    asker_homepage = AskerHomePage(context.asker)
    assert asker_homepage.is_active()
    context.asker_homepage = asker_homepage


@when("I open AskerSignUpModal")
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


@then("TermsConditionsModal should be presented")
def step_impl(context):
    asker_terms_and_conditions_modal = TermsConditionsModal(context.asker)
    assert asker_terms_and_conditions_modal.is_visible()
    context.asker_terms_and_conditions_modal = asker_terms_and_conditions_modal


@when("I press Next")
def step_impl(context):
    assert context.asker_terms_and_conditions_modal.is_element_inside_clickable()
    context.asker_terms_and_conditions_modal.click_next_button()


@then("I should be redirected to AskerHomePage")
def step_impl(context):
    print(context.asker_homepage.browser.driver.current_url)
    assert context.asker_homepage.is_active()


@when("Expert is on ExpertHomePage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Expert is on ExpertHomePage')


@step("Expert presses login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Expert presses login button')


@then("A dropdown should show up")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then A dropdown should show up')


@when("Expert presses Signup")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Expert presses Signup')


@then("The dropdown should show sign up form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then The dropdown should show sign up form')


@when("Expert enters email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Expert enters email')


@step("Expert enters password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Expert enters password')


@step("Expert enters confirm password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Expert enters confirm password')


@step("Expert click Sign Up button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Expert click Sign Up button')


@when("Expert presses Next")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Expert presses Next')


@then("Expert should be redirected to ExpertOnboardPage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Expert should be redirected to ExpertOnboardPage')


@when("Admin bypass that expert")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Admin bypass that expert')


@step("Expert go to ExpertHomePage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Expert go to ExpertHomePage')


@step("Expert press Start Working Button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Expert press Start Working Button')


@then("Expert should see the ExpertWorkspacePage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Expert should see the ExpertWorkspacePage')


@when("I post a question")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I post a question')


@then("Expert should see that question")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Expert should see that question')


@when("Expert claims the question")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Expert claims the question')


@then("I should see ProblemExpertIntroModal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see ProblemExpertIntroModal')


@when("I press GotIt button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I press GotIt button')


@then("I should be in the same room with that expert")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should be in the same room with that expert')
