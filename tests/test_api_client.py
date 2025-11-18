import pytest
from unittest.mock import patch, MagicMock
from api_client import APIClient
@pytest.fixture
def client():
    return APIClient()
def test_get_user_happy_path(client, mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {"profile": {"id": 1, "name": "Alice"}}
    mock_response.status_code = 200
    mocker.patch.object(client.session, "get", return_value=mock_response)
    result = client.get_user(1)
    assert result == {"id": 1, "name": "Alice"}
def test_create_payment_success(client, mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "success"}
    mocker.patch.object(client.session, "post", return_value=mock_response)
    resp = client.create_payment(100, "usd")
    assert resp["status"] == "success"
