import pytest
from data.user_account_repository import UserAccountRepository
from reset_test_db import reset_test_db

@pytest.fixture(autouse=True)
def setup():
    reset_test_db()

def test_find_by_id():
    repository = UserAccountRepository()
    user = repository.find_by_id(1)
    assert user.username == 'wmalita'