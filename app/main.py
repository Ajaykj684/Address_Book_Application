from fastapi import FastAPI
from app.api.address.endpoints import router

app = FastAPI()

app.include_router(router)
