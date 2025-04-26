from typing import Optional
import json
from pydantic import BaseModel, Field

#Request models
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

# Response models
class LoginResponseModel(BaseModel):
    token: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None

class PetResponseModel(BaseModel):
    id: Optional[int] = None



# class OuterResponseModel(BaseModel):
#     class_ = Optional[str] = Field(..., alias='class')
