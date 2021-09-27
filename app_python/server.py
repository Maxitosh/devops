from fastapi import FastAPI

from app_python.routers.current_time import time_router
from app_python.routers.metrics import metrics_router
from app_python.routers.visits import visits_router

app = FastAPI(
    title="Moscow time",
    description="Shows current Moscow time",
)

app.include_router(time_router, prefix="")
app.include_router(metrics_router, prefix="")
app.include_router(visits_router, prefix="/visits")
