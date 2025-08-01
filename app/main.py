from fastapi import FastAPI
from app.config.database import engine
from app.model import school_model
from app.controller import school_controller
from dotenv import load_dotenv

import asyncio

load_dotenv()

app = FastAPI(
    title="School API",
    version="1.0.0",
)

# ✅ Register routes
app.include_router(school_controller.router, prefix="/school", tags=["School"])
