from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from dotenv import load_dotenv
import os

from activity.routes import router as activity_router
from auth.routes import router as auth_router
from health.routes import router as health_router
from meals.routes import router as meals_router
from ml.routes import router as ml_router
from dashboard.routes import router as dashboard_router

# Load environment variables
load_dotenv()

app = FastAPI()

# Get frontend URL
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

print("FRONTEND_URL:", FRONTEND_URL)

origins = [FRONTEND_URL]

# Static uploads
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)
app.include_router(activity_router)
app.include_router(health_router)
app.include_router(meals_router)
app.include_router(ml_router)
app.include_router(dashboard_router)