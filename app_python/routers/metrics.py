from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from pytz import timezone

MOSCOW_TZ = timezone("Europe/Moscow")
metrics_router = APIRouter(prefix="/metrics")


@metrics_router.get("/", response_class=PlainTextResponse)
def metrics() -> str:
    return "True"
