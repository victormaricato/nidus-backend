from fastapi import FastAPI
from backend import controller

app = FastAPI()

app.include_router(controller.router)