from backend.models.preferences import PreferencesInsert
from backend.models.users import UserInsert
from backend.repository.user import UserRepository


def test_user_is_correctly_inserted(user_repository: UserRepository) -> None:
    preferences = PreferencesInsert(integ_anotacoes=0, integ_tarefas=0, integ_lembretes=0, integ_email=0, integ_push=0)

    user_to_insert = UserInsert(
        tw_id=1234,
        tw_token="twitter_token",
        tw_handle="twitter_handle",
        email="email",
        apelido_usuario="apelido_usuario",
    )

    user_id = user_repository.create(user_to_insert, preferences)

    assert isinstance(user_id, int)
