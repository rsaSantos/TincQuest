from fastapi import FastAPI
from .routers.user import user_router

tincQuest = FastAPI()

tincQuest.include_router(user_router.router)