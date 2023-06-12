from backend.service.scheduler import scheduler
from backend.repository.session import SessionRepository
from backend.repository.settings import SettingsRepository
from backend.models.reminders import ReminderModel, ReminderInsert
from backend.repository.reminders import RemindersRepository
from backend.repository.user import UserRepository
from backend.service.tweet import post_tweet
from fastapi import APIRouter, Depends, Header
from uuid import uuid4
from backend.service.sms import send_sms
from backend.service.email import send_email
from datetime import datetime

router = APIRouter(prefix="/reminders")

@router.post("/")
async def post(
    reminder_insert: ReminderInsert,
    authorization: str = Header(None),
    user_id: str = Header(None, convert_underscores=False), 
    reminders_repository: RemindersRepository = Depends(),
    session_repository: SessionRepository = Depends(),
    user_repository: UserRepository = Depends(),
    settings_repository: SettingsRepository = Depends(),
    scheduler = Depends(scheduler)
) -> ReminderModel:
    if(not(session_repository.validate(authorization, user_id))):
      return dict(error="Invalid token.")

    access_token, verifier = user_repository.get_credentials(user_id)

    user = user_repository.find_by_id(user_id)

    settings = settings_repository.find_by_user_id(user_id)

    date = reminder_insert.date[0:10] + ' ' + reminder_insert.date[11:19]

    if(settings.reminder):
      tweet_id = await post_tweet(access_token, verifier, reminder_insert.content)

      reminder = reminders_repository.create(ReminderModel(
      id=uuid4(),
      tweet_id=tweet_id,
      user_id=user_id,
      content=reminder_insert.content,
      date=date
    ))

    reminder = reminders_repository.create(ReminderModel(
      id=uuid4(),
      user_id=user_id,
      content=reminder_insert.content,
      date=date
    ))

    if(settings.email):
      date_parsed = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
      scheduler.add_job(send_email, 'date', run_date=date_parsed, 
      args=[reminder_insert.content, user.tw_email])
        

    if(settings.push):
      date_parsed = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
      scheduler.add_job(send_sms, 'date', run_date=date_parsed, 
      args=[reminder_insert.content, user.phone])

    return reminder