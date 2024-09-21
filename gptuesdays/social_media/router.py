from fastapi import APIRouter

router = APIRouter()

router.post("/api/social-media/general-long-post/")
async def general_long_post():
    pass