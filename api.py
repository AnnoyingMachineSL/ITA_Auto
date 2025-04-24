import requests
import json

import generator
from config import LoginPageConfig, LoginPageSecond
from pprint import pprint


class PetsApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def login(self, request) -> json:
        res = requests.post(url=self.base_url + 'login',
                            data=json.dumps(request))
        return res.json(), res.status_code


    def post_pet(self, email: str, password: str,
                 name: str, pet_type: str,
                 age: int, gender: str) -> json:

        authorization_data, status_code = self.login(email=email, password=password)
        headers = dict(Authorization=f'Bearer {authorization_data["token"]}')

        data = {
            "id": 0,
            "name": name,
            "type": pet_type,
            "age": age,
            "gender": gender,
            "owner_id": authorization_data['id'],
        }

        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        return res.json(), res.status_code


    def get_pet(self, email: str, password: str, pet_id: int):
        authorization_data, status_code = self.login(email, password)
        headers = {'Authorization': f'Bearer {authorization_data["token"]}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        return res.json(), res.status_code


    def post_pet_image(self, email: str, password: str, pet_id: int) -> json:
        authorization_data, status_code = self.login(email, password)
        headers = {'Authorization': f'Bearer {authorization_data["token"]}'}
        img = {'pic': ('parrot.png', open('', 'rb'), 'image/png')}
        files = {'pic': img}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        return res.json(), res.status_code


    def get_pet_list(self,email: str, password: str, len_pet_list: int):
        authorization_data, status_code = self.login(email=email, password=password)
        headers = dict(Authorization=f'Bearer {authorization_data["token"]}')
        user_id = authorization_data['id']
        data = {
                  "num": len_pet_list,
                  "user_id": 5299
                }
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        return res.json(), res.status_code


    def delete_pet(self, email: str, password: str, pet_id: int):
        authorization_data, status_code = self.login(email=email, password=password)
        headers = dict(Authorization=f'Bearer {authorization_data["token"]}')

        res = requests.delete(url=self.base_url + f'pet/{pet_id}', headers=headers)
        return res.json(), res.status_code


    def update_pet(self, email: str, password: str, pet_id: int,
                   pet_name: str, pet_type: str, pet_age: int, pet_gender: str):
        authorization_data, status_code = self.login(email=email, password=password)
        headers = dict(Authorization=f'Bearer {authorization_data["token"]}')
        user_id = authorization_data['id']
        data = {
                  "id": pet_id,
                  "name": pet_name,
                  "type": pet_type,
                  "age": pet_age,
                  "gender": pet_gender,
                  "owner_id": user_id,
                  "pic": "string",
                  "owner_name": "string",
                  "likes_count": 0,
                  "liked_by_user": True
                }

        res = requests.patch(url=self.base_url + 'pet', data=json.dumps(data), headers=headers)
        return res.json(), res.status_code


    def like_pet(self,  email: str, password: str, pet_id: int):
        authorization_data, status_code = self.login(email=email, password=password)
        headers = dict(Authorization=f'Bearer {authorization_data["token"]}')

        res = requests.put(url=self.base_url + f'pet/{pet_id}/like', headers=headers)
        return res.json(), res.status_code


#pt = PetsApi()
# print(pt.get(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD,
#                     pet_id=34028, pet_name='Katana', pet_type='sword', pet_age=999, pet_gender='Female'))
#print(pt.like_pet(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD, pet_id=34361))
# print(pt.get_pet(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD, pet_id=34028))
# print(generator.extract_pet_id(pets_list))
#pprint(pt.delete_pet(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD, pet_id=33776))
# print(new_pet_id, _)
#
# new_pet_data, _ = pt.get_pet(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD, pet_id=new_pet_id['id'])
# print(pt.post_pet_image(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD,
#                         pet_id=new_pet_data['pet']['id']))


