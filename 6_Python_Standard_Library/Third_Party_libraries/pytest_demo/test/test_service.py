import pytest
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
