from fastapi import FastAPI
from .routers.user import user_router
from .routers.event import event_router

tincQuest = FastAPI()

tincQuest.include_router(user_router.router)
tincQuest.include_router(event_router.router)