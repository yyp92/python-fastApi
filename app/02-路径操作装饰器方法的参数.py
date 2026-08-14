# 路径操作装饰器
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post(
    "/items",
    tags=["这是items测试接口"],
    summary="这是items测试接口 summary",
    description="这是items测试接口 description",
    response_description="这是items测试接口 response description",
    # deprecated=True
)
def test():
    return {"items": "items 数据"}


if __name__ == "__main__":
    uvicorn.run(
        "02-路径操作装饰器方法的参数:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
