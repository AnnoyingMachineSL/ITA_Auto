import random
import string


def random_name():
    return ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(5)])

def random_email():
    return random_name() + '@gmail.com'

def random_password():
    return random_name() + ''.join([random.choice(string.digits) for i in range(4)])