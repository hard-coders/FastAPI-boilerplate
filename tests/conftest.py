import pytest
from fastapi.testclient import TestClient

from app import main


@pytest.fixture
def client():
    yield TestClient(main.app)

