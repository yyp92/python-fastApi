# 路径操作装饰器
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def get_test():
    return {"method": "get 方法"}

@app.post("/post")
def post_test():
    return {"method": "post 方法"}

@app.put("/put")
def put_test():
    return {"method": "put 方法"}

@app.delete("/delete")
def delete_test():
    return {"method": "delete 方法"}


if __name__ == "__main__":
    uvicorn.run(
        "01-路径操作装饰器方法:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
