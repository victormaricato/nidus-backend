import tweepy
import os
from uuid import uuid4
from backend.models.user import UserInsert
from backend.models.settings import SettingsInsert
from backend.models.session import SessionInsert
from backend.repository.user import UserRepository
from backend.repository.settings import SettingsRepository
from backend.repository.session import SessionRepository
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/login")

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')


@router.get("/request-token")
async def request_token():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    return auth._get_request_token()


@router.get("/access-token")
async def access_token(oauth_token: str, oauth_token_secret: str, 
oauth_verifier: str, user_repository: UserRepository = Depends(),
settings_repository: SettingsRepository = Depends(),
session_repository: SessionRepository = Depends()
):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.request_token = {
        'oauth_token': oauth_token,
        'oauth_token_secret': oauth_token_secret
    }
    access_token, verifier = auth.get_access_token(verifier=oauth_verifier)
    api = tweepy.API(auth)
    me = api.verify_credentials(include_email=True)

    user = user_repository.find_by_email(getattr(me, 'email'))

    if(user == None):
        user_id = uuid4()
        user_repository.create(UserInsert(
                id=user_id,
                tw_id=getattr(me, 'id'),
                tw_name=getattr(me, 'name'),
                tw_access_token=access_token,
                tw_access_token_verifier=verifier,
                tw_profile_picture=getattr(me, 'profile_image_url'),
                tw_email=getattr(me, 'email')
        ))
        settings_repository.create(SettingsInsert(id=uuid4(), user_id=user_id))
    else:
      user_id = getattr(user, 'id')

    session = SessionInsert(
        id=uuid4(),
        access_token=uuid4(),
        active=True,
        user_id=user_id
        )

    session_repository.create(session)

    return dict(user_id=user_id, session=session)