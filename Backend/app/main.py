from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

app = FastAPI()

# Frontend URL
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

origins = [FRONTEND_URL]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static uploads
if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


# Simple health check (important for Render)
@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}


# Import routers AFTER app creation (prevents slow startup)
from activity.routes import router as activity_router
from auth.routes import router as auth_router
from health.routes import router as health_router
from meals.routes import router as meals_router
from ml.routes import router as ml_router
from dashboard.routes import router as dashboard_router

# Register routers
app.include_router(auth_router)
app.include_router(activity_router)
app.include_router(health_router)
app.include_router(meals_router)
app.include_router(ml_router)
app.include_router(dashboard_router)