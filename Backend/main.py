from fastapi import FastAPI
from .routers.user import user_router
from .routers.event import event_router
from fastapi.middleware.cors import CORSMiddleware

from .database.database import engine 


tincQuest = FastAPI()
origins = ["*"]

tincQuest.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .models import user as user_model
from .models import participant as participant_model
from .models import event as event_model
from .models import prize as prize_model
from .models import question as question_model

user_model.Base.metadata.create_all(bind=engine)
participant_model.Base.metadata.create_all(bind=engine)
event_model.Base.metadata.create_all(bind=engine)
prize_model.Base.metadata.create_all(bind=engine)
question_model.Base.metadata.create_all(bind=engine)


tincQuest.include_router(user_router.router)
tincQuest.include_router(event_router.router)
