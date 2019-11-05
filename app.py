from actors.client import Client
from actors.expert import Expert
from pom.admin.admin_login_page import AdminLoginPage
from pom.expert.expert_sign_up_page import ExpertSignUp
from pom.expert.expert_home_page import ExpertHomepage
from utils.email_gen import generate_email

if __name__ == '__main__':
    email = generate_email('troy')
    password = 'MotConVit123!@'

    expert = Expert()
    expert_signup_page = ExpertSignUp(expert)
    expert_signup_page.sign_up(email, password)

    admin = Client('https://admin-query.got-it.io/')
    page = AdminLoginPage(admin)
    page.login_and_approve_newest_expert()

    expert_home_page = ExpertHomepage(expert)
    expert_home_page.start_working()
