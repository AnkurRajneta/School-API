from fastapi import FastAPI
from app.config.config import Database
from app.config.database import engine
from app.model import school_model
from app.controller import school_controller, auth_controller
from dotenv import load_dotenv

school_model.Base.metadata.create_all(bind = engine)

app = FastAPI(
    title = "School API",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
)


app.include_router(school_controller.router, prefix = "/school", tags = ['School'])
app.include_router(auth_controller.router)