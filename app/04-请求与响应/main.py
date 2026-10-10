# 请求体数据
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05
from apps.app06 import app06
from apps.app07 import app07


app = FastAPI()

# 获取 main.py 所在目录，拼接 statics
base_dir = os.path.dirname(__file__)
static_dir = os.path.join(base_dir, "statics")
# 静态文件
app.mount(
    "/static",
    StaticFiles(directory=static_dir)
)

app.include_router(
    app01,
    tags=["01 路径参数"]
)
app.include_router(
    app02,
    tags=["02 查询参数"]
)
app.include_router(
    app03,
    tags=["03 请求体数据"]
)
app.include_router(
    app04,
    tags=["04 form 表单数据"]
)
app.include_router(
    app05,
    tags=["05 文件上传"]
)
app.include_router(
    app06,
    tags=["06 Request对象"]
)
app.include_router(
    app07,
    tags=["07 响应参数"]
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
