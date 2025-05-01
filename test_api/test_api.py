import allure
import pytest
from urllib3 import request

import generator
from api import PetsApi
from client import Client
from config import LoginPageSecond, LoginPageConfig
from models.pet_models import PetResponseModel, LoginResponseModel, LoginModel, CreatePetModel, GetPetsListModel, \
    PetListResponseModel, PetInfoResponseModel
from valdate_response import ValidateResponse


@allure.title('[Positive] Api Tests')
class TestApi:

    @allure.title('[Api test] Authorization')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    def test_login(self, email: str, password: str):
        login_model = LoginModel(email=email, password=password)
        response = Client().login(request=login_model, expected_model=LoginResponseModel())
        return response

    @allure.title('[Api test] Post pet')
    @pytest.mark.positive
    @pytest.mark.API
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('name', ['aas', 'bbs', 'qwe'])
    @pytest.mark.parametrize('pet_type', ['cat'])
    @pytest.mark.parametrize('age', ['1', '2'])
    @pytest.mark.parametrize('gender', ['male', 'female'])
    def test_post_pet(self, email: str, password: str,
                      name: str, pet_type: str, age: int, gender: str):
        login_model = LoginModel(email=email, password=password)
        authorization_response = Client().login(request=login_model, expected_model=LoginResponseModel())
        headers = dict(Authorization=f'Bearer {authorization_response.token}')
        pet_info_model = CreatePetModel(
            id=0,
            name=name,
            type=pet_type,
            age=age,
            gender=gender,
            owner_id=authorization_response.id)

        created_pet_response = Client().post_pet(request=pet_info_model,
                                                 expected_model=PetResponseModel(),
                                                 headers=headers)
        return created_pet_response

    @allure.title('[Api test] Get pets list')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(name='test_get_pets_list')
    @pytest.mark.dependency(depends='test_post_pet')
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [5])
    def test_get_pets_list(self, email: str, password: str, len_pet_list: int):
        login_model = LoginModel(email=email, password=password)
        authorization_response = Client().login(request=login_model, expected_model=LoginResponseModel())
        headers = dict(Authorization=f'Bearer {authorization_response.token}')

        pets_list_model = GetPetsListModel(
            skip=0,
            num=len_pet_list,
            user_id=authorization_response.id)

        pets_list_response = Client().get_pets_list(request=pets_list_model,
                                                    expected_model=PetListResponseModel(
                                                        list=[CreatePetModel(
                                                            id=None,
                                                            name=None,
                                                            type=None,
                                                            age=None,
                                                            gender=None,
                                                            owner_id=None,
                                                            pic='string',
                                                            owner_name='string',
                                                            likes_count=0,
                                                            liked_by_user=False)]),
                                                    headers=headers)
        return pets_list_response

    @allure.title('[Api test] Delete pet')
    @pytest.mark.positive
    @pytest.mark.API
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.dependency(depends='test_get_pets_list')
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [15])
    def test_delete_pet(self, email: str, password: str, len_pet_list: int):
        pets_id_list = generator.extract_pet_id(self.test_get_pets_list(email, password, len_pet_list))
        login_model = LoginModel(email=email, password=password)
        authorization_response = Client().login(request=login_model, expected_model=LoginResponseModel())
        headers = dict(Authorization=f'Bearer {authorization_response.token}')

        for pet_id in pets_id_list:
            Client().delete_pet(pet_id=pet_id, headers=headers)


    @allure.title('[Api test] Update pet info')
    @pytest.mark.positive
    @pytest.mark.API
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

        pets_id_list = generator.extract_pet_id(self.test_get_pets_list(email, password, len_pet_list))
        login_model = LoginModel(email=email, password=password)
        authorization_response = Client().login(request=login_model, expected_model=LoginResponseModel())
        headers = dict(Authorization=f'Bearer {authorization_response.token}')

        for pet_id in pets_id_list:
            pet_info_model = CreatePetModel(
                                            id=pet_id,
                                            name=pet_name,
                                            type=pet_type,
                                            age=pet_age,
                                            gender=pet_gender,
                                            owner_id=authorization_response.id)
            Client().update_pet(request=pet_info_model,
                                expected_model=PetResponseModel(),
                                headers=headers)

            actual_pet_data = Client().get_pet(pet_id=pet_id, headers=headers)
            expected_pet_data = PetInfoResponseModel(pet=pet_info_model, comments=[])
            ValidateResponse.validate_response(response=actual_pet_data, model=expected_pet_data)

    @allure.title('Api Like pet')
    @pytest.mark.positive
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('email', [LoginPageSecond.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    @pytest.mark.parametrize('len_pet_list', [10])
    def test_like_pet(self, email: str, password: str, len_pet_list: int):

        pets_id_list = generator.extract_not_liked_pet_id(self.test_get_pets_list(email, password, len_pet_list))
        login_model = LoginModel(email=email, password=password)
        authorization_response = Client().login(request=login_model, expected_model=LoginResponseModel())
        headers = dict(Authorization=f'Bearer {authorization_response.token}')

        for pet_id in pets_id_list:
            Client().like_pet(pet_id=pet_id, headers=headers)





# at = TestApi()
# pets_list, _ = at.test_get_pets_list(email=LoginPageSecond.LOGIN,
#                             password=LoginPageSecond.PASSWORD,
#                             len_pet_list=5).json()
# print(at.test_get_pets_list(email=LoginPageSecond.LOGIN,
#                             password=LoginPageSecond.PASSWORD,
#                             len_pet_list=5).json())
#
# print(at.test_delete_pet(email=LoginPageSecond.LOGIN,
#                             password=LoginPageSecond.PASSWORD,
#                             len_pet_list=5))
