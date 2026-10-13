from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()


# @app.middleware("http")
# async def MyCORSMiddleware(request: Request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/user")
async def get_user():
    return {
        "user": "current user"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8080,
        reload=True,
        log_level="debug"
    )
