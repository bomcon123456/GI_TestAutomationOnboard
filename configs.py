import os

from dotenv import load_dotenv

load_dotenv()

ASKER_EMAIL_PREFIX = os.getenv('ASKER_EMAIL_PREFIX')
EXPERT_EMAIL_PREFIX = os.getenv('EXPERT_EMAIL_PREFIX')
PASSWORD_COMMON = os.getenv('PASSWORD_COMMON')
ASKER_URL = os.getenv('ASKER_URL')
EXPERT_URL = os.getenv('EXPERT_URL')
ADMIN_URL = os.getenv('ADMIN_URL')
GMAIL_ACCOUNT = os.getenv('GMAIL_ACCOUNT')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
