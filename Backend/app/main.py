from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import traceback
import asyncio
import httpx

# Load environment variables
load_dotenv()

app = FastAPI()

@app.on_event("startup")
async def start_keep_awake():
    async def ping_server():
        while True:
            await asyncio.sleep(300) # Wait 5 minutes
            url = os.getenv("RENDER_EXTERNAL_URL")
            if url:
                try:
                    async with httpx.AsyncClient() as client:
                        await client.get(f"{url}/health")
                        print(f"Keep-awake ping sent to {url}/health")
                except Exception as e:
                    print(f"Keep-awake ping failed: {e}")

    asyncio.create_task(ping_server())

# Allowed frontend origins
origins = [
    "http://localhost:5173",
    "https://bio-sync-sandy.vercel.app",
]

# CORS Middleware — must be added BEFORE exception handlers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.(vercel\.app|onrender\.com)",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler — ensures CORS headers are present even on 500 errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Unhandled exception on {request.method} {request.url}: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)},
    )

# Ensure uploads folder exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Static uploads
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Root endpoint (helps Render detect the service)
@app.get("/")
def root():
    return {"status": "API running"}

# Health endpoint
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