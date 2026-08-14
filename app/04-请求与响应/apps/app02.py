# 查询参数
from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()

@app02.get("/job/{kd}")
async def get_jobs(kd: str, xl: Union[str, None] = None, gj: Optional[str] = None):
    # 路径参数： kd
    # 查询参数： xl, gj
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }