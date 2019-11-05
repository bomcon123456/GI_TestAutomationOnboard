import time


def generate_email(prefix):
    return prefix + '_' + str(int(time.time())) + '@gmail.com'
