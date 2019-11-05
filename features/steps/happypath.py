import time

from behave import *

from actors.expert import Expert
from actors.asker import Asker
from actors.client import Client
from pom.admin.admin_login_page import AdminLoginPage
from pom.asker.asker_home_page import AskerHomePage
from pom.asker.asker_sign_up_page import AskerSignUp
from pom.expert.expert_home_page import ExpertHomepage
from pom.expert.expert_work_page import ExpertWorkPage
from pom.expert.expert_sign_up_page import ExpertSignUp
from utils.email_gen import generate_email

use_step_matcher("re")


@given("Asker/ Expert signed up, Expert has been approved and start working")
def step_impl(context):
    asker_email = generate_email('troy')
    expert_email = generate_email('etroy')
    password = 'MotConVit123!@'

    asker = Asker()
    asker_signup_page = AskerSignUp(asker)
    asker_signup_page.sign_up(asker_email, password)

    expert = Expert()
    expert_signup_page = ExpertSignUp(expert)
    expert_signup_page.sign_up(expert_email, password)

    admin = Client('https://admin-query.got-it.io/')
    page = AdminLoginPage(admin)
    page.login_and_approve_newest_expert()

    expert_home_page = ExpertHomepage(expert)
    expert_home_page.start_working()

    context.asker = asker
    context.expert = expert


@when("Asker post a quest then Expert bids and claims the question")
def step_impl(context):
    asker_home_page = AskerHomePage(context.asker)
    asker_home_page.query()

    expert_work_page = ExpertWorkPage(context.expert)
    expert_work_page.claim_question()


@then("Asker and Expert are in a chat session")
def step_impl(context):
    asker = context.asker
    expert = context.expert
    time.sleep(10)
