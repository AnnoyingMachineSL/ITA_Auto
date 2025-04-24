import allure
import requests

from allure_helper import AllureHelper
from models.pet_models import LoginModel, validate_response, LoginResponseModel
from dotenv import load_dotenv
import os


class ClientApi:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.session =self._initialize_session()

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self, method: str, url: str, json):
        response = self.session.request(method=method,
                                        url=self.base_url + url,
                                        json=json)
        AllureHelper().enrich_allure(response)
        return response


class Client(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step('POST /login')
    def login(self, request: LoginModel, expected_model: LoginResponseModel, status_code: int = 200):
        response = self.request(method='post', url='/login', json=request.model_dump())
        return validate_response(response=response, model=expected_model, status_code=status_code)
