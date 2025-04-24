from typing import Optional

from pydantic import BaseModel, Field


def validate_response(response, model, status_code):
    assert response.status_code == status_code
    return model.model_validate(response)


class LoginResponseModel(BaseModel):
    token: Optional[str]
    email: Optional[str]
    id: Optional[int]


class PetResponseModel(BaseModel):
    id: int


class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]

# class OuterResponseModel(BaseModel):
#     class_ = Optional[str] = Field(..., alias='class')
