from fastapi import FastAPI
from activity.routes import router as activity_router
from auth.routes import router as auth_router

app = FastAPI()

app.include_router(activity_router)
app.include_router(auth_router)
