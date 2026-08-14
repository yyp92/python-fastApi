# 路径参数
from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/user/{id}")
def get_user(id: str):
    print('id', id, type(id))

    return {
        "user_id": id
    }
