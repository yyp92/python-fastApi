from fastapi import FastAPI, Request, Response
import uvicorn
import time


app = FastAPI()


# 中间件
@app.middleware("http")
async def m2(request: Request, call_next):
    # 请求代码块
    print("m2 request")
    response = await call_next(request)

    # 响应代码块
    response.headers["author"] = "yuan"
    print("m2 response")

    return response

@app.middleware("http")
async def m1(request: Request, call_next):
    # 请求代码块
    print("m1 request")
    # ip 限制
    # if request.client.host in ["127.0.0.1", "localhost"]:
    #     return Response(
    #         # status_code=1001,
    #         content="forbidden",
    #     )

    # 路径限制
    # if request.url.path in ["/user"]:
    #     return Response(
    #         # status_code=1001,
    #         content="forbidden",
    #     )

    start = time.time()

    response = await call_next(request)

    # 响应代码块
    print("m1 response")
    end = time.time()
    response.headers["process-time"] = str(end - start)

    return response


@app.get("/user")
async def get_user():
    time.sleep(3)
    print("get_user 函数执行")

    return {
        "user": "current user"
    }

@app.get("/item/{item_id}")
async def get_item(item_id: int):
    time.sleep(2)
    print("get_item 函数执行")

    return {
        "item_id": item_id
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
