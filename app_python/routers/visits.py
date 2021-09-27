from fastapi import APIRouter
from fastapi.responses import PlainTextResponse


visits_router = APIRouter(
    tags=["visits"],
)


@visits_router.get("/", response_class=PlainTextResponse)
def get_visits() -> str:
    with open('/home/myuser/app_python/media/media.txt', 'r') as file:
        return "\n".join(file.readlines())
