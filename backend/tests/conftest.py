from backend.repository.register import RegisterRepository
from backend.repository.task import TaskRepository
from backend.repository.task_list import TaskListRepository
from backend.repository.user import UserRepository
from backend.service.task import TaskService
from pytest import fixture


@fixture
def register_repository() -> RegisterRepository:
    return RegisterRepository()


@fixture
def task_list_repository() -> TaskListRepository:
    return TaskListRepository()


@fixture
def user_repository() -> UserRepository:
    return UserRepository()


@fixture
def task_repository() -> TaskRepository:
    return TaskRepository()


@fixture
def task_service(task_repository: TaskRepository) -> TaskService:
    return TaskService(task_repository)
