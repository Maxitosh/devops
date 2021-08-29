import pytest
from starlette.testclient import TestClient

from app_python.server import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client
