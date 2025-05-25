import pytest
import requests

# proper import of the package matters a lot, wasted 2 days for it.
from ..source import c_service
import unittest.mock as mock


@mock.patch(c_service.__name__ + ".get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    """
    mock_get_user_from_db: This is a simple random string
    """
    mock_get_user_from_db.return_value = "Mocked Madhu"
    user_name = c_service.get_user_from_db(1)
    assert user_name == "Mocked Madhu"


@mock.patch("requests.get")
def test_get_user(mock_get):
    """
    Testing API success scenario
    """
    # Creates a mock object to simulate the response object returned
    # by the requests.get method.
    mock_response = mock.Mock()
    # Sets the status code of the mock response to 200,
    # indicating a successful HTTP response.
    mock_response.status_code = 200
    #  Sets the return value of the json method of the mock response to a
    #  dictionary, simulating the JSON data returned by the API.
    mock_response.json.return_value = {"id": 1, "name": "Madhu"}
    # print(f"\nmock_response: {mock_response}")
    # Configures the mock requests.get method to return the mock
    # response when called.
    mock_get.return_value = mock_response
    # Calls the get_user function from your module, which internally
    # calls requests.get, but in this test, it gets the mocked response.
    data = c_service.get_user()
    # print(f"\nData: {data}")
    assert data == {"id": 1, "name": "Madhu"}


@mock.patch("requests.get")
def test_get_user_error(mock_get):
    """
    Testing the failure scenario
    """
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.exceptions.HTTPError):
        c_service.get_user()