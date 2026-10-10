# Request对象
from fastapi import APIRouter, Request

app06 = APIRouter()

@app06.post("/request")
async def get_request(request: Request):
    print("request", request.scope)

    return {
        "url": request.url
    }