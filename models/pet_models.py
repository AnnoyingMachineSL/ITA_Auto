from typing import Optional
import json
from pydantic import BaseModel, Field


# Request models
class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]


class CreatePetModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    type: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    owner_id: Optional[int]
    pic: Optional[str] = 'string'
    owner_name: Optional[str] = 'string'
    likes_count: Optional[int] = 0
    liked_by_user: Optional[bool] = False


class GetPetsListModel(BaseModel):
    skip: Optional[int] = 0
    num: Optional[int]
    user_id: Optional[int]


# Response models
class LoginResponseModel(BaseModel):
    token: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None


class PetResponseModel(BaseModel):
    id: Optional[int] = None


class PetListResponseModel(BaseModel):
    list: Optional[list[CreatePetModel]]
    total: Optional[int] = None

class PetInfoResponseModel(BaseModel):
    pet: CreatePetModel
    comments: Optional[list]


#Negative response models

class NegativeLoginResponseModel(BaseModel):
    detail: Optional[str] = 'Username is taken or pass issue'

class NegativePetsListModel(BaseModel):
    detail: Optional[list] = [
        {loc: Optional[]}
    ]
    # "detail": [
    #     {
    #         "loc": [
    #             "body",
    #             23
    #         ],
    #         "msg": "Expecting value: line 3 column 9 (char 23)",
    #         "type": "value_error.jsondecode",
    #         "ctx": {
    #             "msg": "Expecting value",
    #             "doc": "{\n  \"skip\": 0,\n  \"num\":'3',\n  \"user_id\": 5299\n}",
    #             "pos": 23,
    #             "lineno": 3,
    #             "colno": 9
    #         }
    #     }
    # ]

# class OuterResponseModel(BaseModel):
#     class_ = Optional[str] = Field(..., alias='class')
