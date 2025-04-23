import allure
import pytest

import generator
from api import PetsApi
from config import LoginPageSecond, LoginPageConfig



@allure.title('[Positive] Api Tests')
class TestApi:

    @allure.title('Api Authorization test')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    def test_login(self, email: str, password: str):
        with allure.step(f'Authorization by email:{email} and password:{password}'):
            authorization_data, status_code = PetsApi().login(email=email, password=LoginPageSecond.PASSWORD)
        assert status_code == 200


    @allure.title('Api Make new pet test')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(name='test_post_pet')
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('name', ['aas', 'bbs', 'qwe'])
    @pytest.mark.parametrize('pet_type', ['cat'])
    @pytest.mark.parametrize('age', ['1', '2'])
    @pytest.mark.parametrize('gender', ['male', 'female'])
    def test_post_pet(self, email: str, password: str,
                      name: str, pet_type: str, age: int, gender: str):
        with allure.step(f'Create new pet for user with:{email} and password:{password}.'
                         f'Pet data: name:{name}, pet_type:{pet_type}, age:{age}, gender:{gender}'):
            new_pet_id, status_code = PetsApi().post_pet(email=email, password=password,
                                                         name=name, pet_type=pet_type,
                                                         age=age, gender=gender)
        assert status_code == 200
        assert isinstance(new_pet_id['id'], int)


    @allure.title('Api Make new pet test')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(name='test_get_pets_list')
    @pytest.mark.dependency(depends='test_post_pet')
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [5])
    def test_get_pets_list(self, email: str, password: str, len_pet_list: int):
        with allure.step(f'Get list of {len_pet_list} pets for user {email}'):
            pets_list, pets_list_status_code = PetsApi().get_pet_list(email=email, password=password,
                                                                      len_pet_list=len_pet_list)
        assert pets_list_status_code == 200
        assert len(pets_list['list']) == len_pet_list


    @allure.title('Api Delete pet')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends='test_get_pets_list')
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [15])
    def test_delete_pet(self, email: str, password: str, len_pet_list: int):
        with allure.step(f'Get pets list for user {email}'):
            pets_list, status_code = PetsApi().get_pet_list(email=email, password=password, len_pet_list=len_pet_list)

        for pet_id in generator.extract_pet_id(pets_list):
            with allure.step(f'Delete pet by id {pet_id}'):
                _, delete_status_code = PetsApi().delete_pet(email=email, password=password, pet_id=pet_id)
            assert delete_status_code == 200


    @allure.title('Api Update info about pet')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [3])
    @pytest.mark.parametrize('pet_name', ['Katana'])
    @pytest.mark.parametrize('pet_type', ['Sword'])
    @pytest.mark.parametrize('pet_age', [100])
    @pytest.mark.parametrize('pet_gender', ['Female'])
    def test_update_pet_info(self, email: str, password: str, len_pet_list: int,
                             pet_name: str, pet_type: str, pet_age: int, pet_gender: str):

        with allure.step('Get some pets from user list'):
            pets_list, pets_list_status_code = PetsApi().get_pet_list(email=email, password=password,
                                                                      len_pet_list=len_pet_list)
        pets_ids = generator.extract_pet_id(pets_list)

        for pet_id in pets_ids:
            with allure.step(f'Update pet data on id {pet_id}'):
                new_pet_id, status_code = PetsApi().update_pet(email=email, password=password, pet_id=pet_id,
                                                               pet_name=pet_name, pet_type=pet_type,
                                                               pet_age=pet_age, pet_gender=pet_gender)
            assert status_code == 200

            with allure.step('Get new information aboun pets after updating'):
                pet_data, get_pet_status_code = PetsApi().get_pet(email=email, password=password, pet_id=pet_id)
                assert get_pet_status_code == 200
                pet_info = pet_data['pet']

            with allure.step('Checking information about a pet'):
                assert pet_info['id'] == pet_id
                assert pet_info['name'] == pet_name
                assert pet_info['type'] == pet_type
                assert pet_info['age'] == pet_age
                assert pet_info['gender'] == pet_gender



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


    @allure.title('Get pets list by incorrect len')
    @pytest.mark.negative
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', ['qwe', '', -2, "!@#!@#"])
    def test_pets_list_incorrect_len(self, email: str, password: str, len_pet_list: int):
        with allure.step(f'Get list of {len_pet_list} pets for user {email}'):
            pets_list, pets_list_status_code = PetsApi().get_pet_list(email=email, password=password,
                                                                      len_pet_list=len_pet_list)
        assert pets_list_status_code == 422


    @allure.title('Delete pet by incorrect id')
    @pytest.mark.negative
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('pet_id', ['', 'a', -4, '!@#!@#'])
    def test_delete_pet_incorrect_id(self, email: str, password: str, pet_id):
        with allure.step(f'Delete pet by id {pet_id}'):
            _, delete_status_code = PetsApi().delete_pet(email=email, password=password, pet_id=pet_id)
            if not len(pet_id):
                assert delete_status_code == 405
            else:
                assert delete_status_code == 422


    @allure.title('Delete pet by id from other user')
    @pytest.mark.negative
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('first_email', [LoginPageConfig.LOGIN])
    @pytest.mark.parametrize('first_password', [LoginPageConfig.PASSWORD])
    @pytest.mark.parametrize('second_email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('second_password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [1])
    def test_delete_pet_from_someone_account(self, first_email: str, first_password: str,
                                             second_email: str, second_password: str, len_pet_list: int):

        with allure.step(f'Get list of {len_pet_list} pets for user {first_email}'):
            pets_list, pets_list_status_code = PetsApi().get_pet_list(email=first_email, password=first_password,
                                                                      len_pet_list=len_pet_list)
        assert pets_list_status_code == 200
        assert len(pets_list['list']) == len_pet_list

        for pet_id in generator.extract_pet_id(pets_list):
            with allure.step(f'Delete pet on user {second_email} by id {pet_id} from other user'):
                _, delete_status_code = PetsApi().delete_pet(email=second_email, password=second_password,
                                                             pet_id=pet_id)

            # предполагаю, что обрадотка такого случая должна отдавать 403
            assert delete_status_code == 403
