from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import os


app = FastAPI()

base_dir = os.path.dirname(__file__)
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))

@app.get("/index")
async def index(request: Request):
    username = "root"
    age = 16
    books = [
        {
            "title": "西游记",
            "price": 400
        },
        {
            "title": "红楼梦",
            "price": 199
        },
        {
            "title": "水浒传",
            "price": 200
        },
        {
            "title": "三国演义",
            "price": 399
        },
    ]
    person = {
        "name": "猪猪",
        "age": 30,
        "gender": "男"
    }
    pi = 3.1415926
    movies = {
        "chengnianren": ["电影", "电视剧", "纪录片"],
        "qingshaonian": ["熊出没", "汪汪队", "海底小纵队"]
    }

    return templates.TemplateResponse(
        # 第一个参数必须是 request 对象
        request, 

        # 模板文件
        "index.html",

        # context 上下文对象，一个字典
        {
            "username": username,
            "age": age,
            "books": books,
            "person": person,
            "pi": pi,
            "movies": movies
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
