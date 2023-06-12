import tweepy
import os

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

async def post_tweet(access_token: str, verifier: str, content: str) -> str:
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
  auth.set_access_token(access_token, verifier)
  api = tweepy.API(auth)
  status = api.update_status(content)
  return getattr(status, 'id_str')

async def delete_tweet(access_token: str, verifier: str, id: str):
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
  auth.set_access_token(access_token, verifier)
  api = tweepy.API(auth)
  api.destroy_status(id)
