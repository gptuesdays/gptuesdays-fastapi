from dotenv import load_dotenv
load_dotenv()
import os

LOCAL_OR_STAGING_OR_PROD=os.getenv("LOCAL_OR_STAGING_OR_PROD")