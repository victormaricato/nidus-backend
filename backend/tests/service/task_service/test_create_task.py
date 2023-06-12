from backend.models.preferences import PreferencesInsert
from backend.models.register import RegisterCreate
from backend.models.task import TaskCreate
from backend.models.task_list import TaskListCreate
from backend.models.users import UserInsert
from backend.repository.register import RegisterRepository
from backend.repository.task_list import TaskListRepository
from backend.repository.user import UserRepository
from backend.service.task import TaskService


def test_task_is_correctly_created(
    task_service: TaskService,
    register_repository: RegisterRepository,
    task_list_repository: TaskListRepository,
    user_repository: UserRepository,
) -> None:
    # Arrange
    user_id = user_repository.create(
        UserInsert(
            tw_id=42,
            tw_token="some-token",
            tw_handle="some-handle",
            apelido_usuario="some-nick",
            email="some-email",
        ),
        PreferencesInsert(integ_anotacoes=0, integ_tarefas=0, integ_lembretes=0, integ_email=0, integ_push=0),
    )
    register_id = register_repository.create(
        RegisterCreate(tweet_content="some_content", tweet_id=0, usuario_id=user_id)
    )
    task_list_id = task_list_repository.create(TaskListCreate(registro_id=register_id))
    task = TaskCreate(texto_tarefa="Teste", lista_id=task_list_id)

    task_id = task_service.create(task)

    assert isinstance(task_id, int)
