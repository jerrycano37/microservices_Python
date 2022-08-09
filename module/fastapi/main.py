import uvicorn as uvicorn
from fastapi import FastAPI

from module.fastapi.routes import welcome


def create_app():
    app = FastAPI()
    app.include_router(welcome.hello_fastapi)
    return app


def start_fastapi():
    fastapi = create_app()
    uvicorn.run(fastapi, host='127.0.0.1', port=8000)
