from fastapi import FastAPI
from activity.routes import router as activity_router
from auth.routes import router as auth_router
from health.routes import router as health_router
from ml.routes import router as ml_router


app = FastAPI()

app.include_router(activity_router)
app.include_router(auth_router)


app.include_router(health_router)

app.include_router(ml_router)
