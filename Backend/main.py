from fastapi import FastAPI
from .routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware


tincQuest = FastAPI()
origins = ["*"]

tincQuest.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


tincQuest.include_router(user_router.router)
