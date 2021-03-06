import os
from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from pytz import timezone

MOSCOW_TZ = timezone("Europe/Moscow")
time_router = APIRouter()


@time_router.get("/", response_class=PlainTextResponse)
def get_time() -> str:
    """
    Show current datetime in Moscow
    """
    current_time = datetime.now(tz=MOSCOW_TZ).isoformat()

    writepath = '/home/myuser/app_python/media/media.txt'

    mode = 'a+' if os.path.exists(writepath) else 'w'

    with open(writepath, mode) as file:
        file.write(current_time + '\n')

    return current_time
