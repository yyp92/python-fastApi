# 请求体数据
from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_api


app = FastAPI()

app.include_router(
    student_api,
    prefix="/student",
    tags=["学生接口"]
)

# 注册 tortoise 框架
# 该方法会在 fastapi 启动时触发，内部通过传递进去的 app 对象，监听服务启动和终止事件
# 当检测到启动事件时，会初始化 Tortoise 对象，如果 generate_schemas=True 则还会进行数据库迁移
# 当检测到终止事件时，会关闭连接
register_tortoise(
    app,
    config = TORTOISE_ORM,

    # 如果数据库为空，则自动生成对应的表单，生产环境不要开
    # generate_schemas=True,
    
    # 生产环境不要开，会泄露调试信息
    # add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
