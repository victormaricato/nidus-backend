from backend.repository.session import SessionRepository
from backend.repository.settings import SettingsRepository
from backend.models.tasklists import TasklistModel, TasklistInsert, TaskModel
from backend.repository.tasklists import TasklistsRepository
from backend.repository.tasks import TasksRepository
from backend.repository.user import UserRepository
from backend.service.tweet import post_tweet
from fastapi import APIRouter, Depends, Header, Request
from uuid import uuid4

router = APIRouter(prefix="/tasklists")

@router.post("/")
async def post(
    tasklist_insert: TasklistInsert,
    authorization: str = Header(None),
    user_id: str = Header(None, convert_underscores=False), 
    tasklists_repository: TasklistsRepository = Depends(),
    tasks_repository: TasksRepository = Depends(),
    session_repository: SessionRepository = Depends(),
    user_repository: UserRepository = Depends(),
    settings_repository: SettingsRepository = Depends()
) -> TasklistModel:
    if(not(session_repository.validate(authorization, user_id))):
      return dict(error="Invalid token.")

    access_token, verifier = user_repository.get_credentials(user_id)

    settings = settings_repository.find_by_user_id(user_id)

    tasklist_content = tasklist_insert.content + '\n' + '\n'\
      .join(tasklist_insert.tasks)

    if(settings.task):
      tweet_id = await post_tweet(access_token, verifier, tasklist_content)

      tasklist = tasklists_repository.create(TasklistModel(
      id=uuid4(),
      tweet_id=tweet_id,
      user_id=user_id,
      content=tasklist_insert.content,
      ))

      for task in tasklist_insert.tasks:
        tasks_repository.create(TaskModel(
        id=uuid4(),
        tasklist_id=tasklist.id,
        complete=False,
        content=task
      ))
    else: 
      tasklist = tasklists_repository.create(TasklistModel(
        id=uuid4(),
        user_id=user_id,
        content=tasklist_insert.content,
      ))

      for task in tasklist_insert.tasks:
        tasks_repository.create(TaskModel(
        id=uuid4(),
        tasklist_id=tasklist.id,
        complete=False,
        content=task
      ))


    return tasklists_repository.find_by_id(tasklist.id)

@router.get("/")
async def get(user_id: str, 
tasklists_repository: TasklistsRepository = Depends()):
  return tasklists_repository.find_by_user_id(user_id)

@router.delete("/")
async def delete(tasklist_id: str, 
tasklists_repository: TasklistsRepository = Depends()):
  return tasklists_repository.delete_by_id(tasklist_id)