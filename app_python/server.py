from fastapi import FastAPI

from app_python.routers.current_time import time_router

app = FastAPI(
    title="Moscow time",
    description="Shows current Moscow time",
)

app.include_router(time_router, prefix="")
