from fastapi import APIRouter

hello_fastapi = APIRouter(prefix="/hello")


@hello_fastapi.get("/")
async def root():
    return {"message": "Hello World"}
