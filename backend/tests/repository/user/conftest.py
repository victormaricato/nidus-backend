from backend.repository.user import UserRepository
from pytest import fixture


@fixture
def user_repository() -> UserRepository:
    return UserRepository()
