# 请求体数据
from fastapi import APIRouter
from typing import Union, Optional, List
from pydantic import BaseModel, Field, field_validator
from datetime import date

app03 = APIRouter()

class Addr(BaseModel):
    province: str
    city: str

class User(BaseModel):
    # name: str = "root"
    # name: str = Field(regex="^a")
    name: str
    age: int = Field(default=18, gt=0, lt=100)
    birth: Union[date, None] = None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value: str):
        # str.isalpha() 判断字符串全部由字母组成
        if not value.isalpha():
            raise ValueError("name must be alpha")
        return value
    
class Data(BaseModel):
    data: List[User]

@app03.post("/user")
async def get_user(user: User):
    return user

@app03.post("/data")
async def get_data(data: Data):
    return data
