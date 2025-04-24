from dotenv import load_dotenv
import os

class LoginPageConfig:
    LOGIN_PAGE_URL = os.getenv('LOGIN_PAGE_URL')
    LOGIN = os.getenv('LOGIN_1')
    PASSWORD = os.getenv('PASSWORD')

class LoginPageSecond:
    LOGIN = os.getenv('LOGIN_2')
    PASSWORD = os.getenv('PASSWORD')

