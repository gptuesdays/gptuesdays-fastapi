import logging
import os

from fastapi import FastAPI, Request, APIRouter
from dotenv import load_dotenv
from gptuesdays import constants
from gptuesdays.social_media import router as social_media_router 

load_dotenv()

if constants.LOCAL_OR_STAGING_OR_PROD == "local":
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(social_media_router.router)

@app.get("/api/hello-world/")
async def hello_world(request: Request):
    return {"message": "Hello, World! I'm GPTuesday!"}