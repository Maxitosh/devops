from datetime import datetime

import pytest
from fastapi import status
from pytz import timezone


@pytest.mark.parametrize(
    ("set_time",),
    [
        ("2021-08-29 12:34",),
        ("2021-08-28 23:59",),
    ],
)
def test_get_time(client, freezer, set_time):
    freezer.move_to(set_time)
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK

    time = datetime.fromisoformat(response.text)
    assert time == datetime.now(tz=timezone("Europe/Moscow"))
