import requests
import json

from config import LoginPageConfig


class PetsApi:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def login(self) -> json:
        data = {
            'email': 'anima@mail.com',
            'password': 'qwe123'
        }

        res = requests.post(url=self.base_url + 'login',
                            data=json.dumps(data))
        token = res.json()['token']
        id = res.json()['id']
        status_code = res.status_code
        return token, id, status_code


    def post_pet(self, name: str, pet_type: str, age: int, gender: str) -> json:
        token, id, status_code = self.login()
        headers = {'Authorization': f'Bearer {token}'}
        data = {
            "id": 0,
            "name": name,
            "type": pet_type,
            "age": age,
            "gender": gender,
            "owner_id": id,
        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        return res.json()['id'], res.status_code

    def get_pet(self, pet_id: int):
        token, _, _ = self.login()
        headers = {'Authorization': f'Bearer {token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        return res.json(), res.status_code


    def post_pet_image(self, pet_id: int) -> json:
        token, id, status_code = self.login()
        headers = {'Authorization': f'Bearer {token}'}
        img = open('jpg_1.JPG', 'rb')
        files = {'pic': img}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        return res.json(), res.status_code


pt = PetsApi()
print(pt.post_pet_image(pet_id=33775))

