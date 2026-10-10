# 响应参数
from fastapi import APIRouter, Response
from pydantic import BaseModel, EmailStr
from typing import Union, List

app07 = APIRouter()

class UserInfo(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {
        "name": "Foo",
        "price": 50.2
    },
    "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2
    },
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": []
    },
}


@app07.post(
    "/userInfo",
    # response_model 是路径操作的参数，并不是路径函数的参数
    response_model = UserOut
)
async def create_user(user: UserInfo):
    return user

@app07.get(
    "/items/{item_id}",
    response_model = Item,
    # 仅返回显示设定的值
    # response_model_exclude_unset = True,
    # 排除 None 值
    # response_model_exclude_none=True,
    # 排除默认值
    # response_model_exclude_defaults=True,
    # 排除 xx 字段
    # response_model_exclude={"tax"},
    # 包含 xx 字段
    # response_model_include={"name", "price"}, 
)
async def read_item(item_id: str):
    return items[item_id]
