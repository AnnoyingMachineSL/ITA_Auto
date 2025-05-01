from typing import Optional
import json
from pydantic import BaseModel, Field


# Request models
class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]


class CreatePetModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    owner_id: Optional[int] = None
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


# class OuterResponseModel(BaseModel):
#     class_ = Optional[str] = Field(..., alias='class')
