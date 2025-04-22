import requests
import json
from config import LoginPageConfig, LoginPageSecond


class PetsApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def login(self, email: str, password: str) -> json:
        data = {
            'email': email,
            'password': password
        }

        res = requests.post(url=self.base_url + 'login',
                            data=json.dumps(data))
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
        img = open('pic.jpg', 'rb')
        files = {'pic': img}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        return res.json(), res.status_code


pt = PetsApi()
new_pet_id, _ = pt.post_pet(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD,
                  name='Baton', pet_type='dog',
                  age=2, gender= 'Male')
print(new_pet_id, _)
#
# new_pet_data, _ = pt.get_pet(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD, pet_id=new_pet_id['id'])
# print(pt.post_pet_image(email=LoginPageSecond.LOGIN, password=LoginPageSecond.PASSWORD,
#                         pet_id=new_pet_data['pet']['id']))


