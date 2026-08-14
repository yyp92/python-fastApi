# form 表单数据
from fastapi import APIRouter, Form

app04 = APIRouter()

@app04.post("/regin")
async def regin(
    username: str = Form(),
    password: str = Form()
):
    print("username: {username}, password: {password}")
    return {
        "username": username
    }
