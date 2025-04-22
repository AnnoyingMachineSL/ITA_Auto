import allure
import pytest
from api import PetsApi
from config import LoginPageSecond


@allure.title('[Positive] Api Tests')
class TestApi:

    @allure.title('Api Authorization test')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    def test_login(self, email: str, password:str):
        with allure.step(f'Authorization by email:{email} and password:{password}'):
            authorization_data, status_code = PetsApi().login(email=email, password=LoginPageSecond.PASSWORD)
        assert status_code == 200


    @allure.title('Api Make new pet test')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('name', ['aas', 'bbs', 'qwe'])
    @pytest.mark.parametrize('pet_type', ['dog', 'cat'])
    @pytest.mark.parametrize('age', ['1', '2', '3'])
    @pytest.mark.parametrize('gender', ['male', 'female'])
    def test_post_pet(self, email: str, password:str,
                      name: str, pet_type: str, age: int, gender: str):
        with allure.step(f'Create new pet for user with:{email} and password:{password}.'
                         f'Pet data: name:{name}, pet_type:{pet_type}, age:{age}, gender:{gender}'):

            new_pet_id, status_code = PetsApi().post_pet(email=email, password=password,
                                                        name=name, pet_type=pet_type,
                                                        age=age, gender=gender)
        assert status_code == 200
        assert isinstance(new_pet_id['id'], int)


@allure.title('[Negative] Api negative tests')
class TestApiNegative:

    @allure.title('Authorization by incorrect password')
    @pytest.mark.negative
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', ['', 'a', 'zxc', '123123'])
    def test_login_incorrect_password(self, email: str, password: str):
        with allure.step(f'Authorization by incorrect password:{password} for user:{email}'):
            authorization_data, status_code = PetsApi().login(email=email, password=password)
        assert status_code == 400


    @allure.title('Authorization by incorrect email')
    @pytest.mark.negative
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', ['', 'a', '123', '@gmail.com'])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    def test_login_incorrect_email(self, email: str, password: str):
        with allure.step(f'Authorization by incorrect email:{email}'):
            authorization_data, status_code = PetsApi().login(email=email, password=password)
        assert status_code == 400