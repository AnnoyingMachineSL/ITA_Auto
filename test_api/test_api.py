import pytest

from api import PetsApi


class TestApi:

    def test_login(self):
        token, id, status_code = PetsApi().login()
        assert status_code == 200

    @pytest.mark.parametrize('name', ['aas', 'bbs', 'qwe'])
    @pytest.mark.parametrize('pet_type', ['dog', 'cat'])
    @pytest.mark.parametrize('age', ['1', '2', '3'])
    @pytest.mark.parametrize('gender', ['male', 'female'])
    def test_post_pet(self, name: str, pet_type: str, age: int, gender: str):
        id, status_code = PetsApi().post_pet(name=name, pet_type=pet_type,
                                                               age=age, gender=gender)
        assert status_code == 200
        assert isinstance(id, int)

class TestApiNegative:

    def test_login_incorrect_password(self, password):
        token, id, status_code = PetsApi().login()
