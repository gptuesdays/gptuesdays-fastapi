import logging
import os

from fastapi import FastAPI, Request, APIRouter
from dotenv import load_dotenv
from src import constants

load_dotenv()

router = APIRouter()

if constants.LOCAL_OR_STAGING_OR_PROD == "local":
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)

@router.get("/api/hello-world/")
async def hello_world(request: Request):
    return {"message": "Hello, World! I'm GPTuesday!"}