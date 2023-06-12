from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, DateTime

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True)
    phone = Column(String)
    tw_id = Column(String)
    tw_name = Column(String)
    tw_access_token = Column(String)
    tw_access_token_verifier = Column(String)
    tw_profile_picture = Column(String)
    tw_email = Column(String)
    created_at = Column(TIMESTAMP, server_default=now())
    settings = relationship("Settings", backref="user", lazy='joined')
    notes = relationship("Note", backref="user", lazy='joined')
    reminders = relationship("Reminder", backref="user", lazy='joined')
    tasklists = relationship("Tasklist", backref="user", lazy='joined')
    session = relationship("Session", backref="user", lazy='joined')


class Settings(Base):
    __tablename__ = "settings"
    id = Column(String, primary_key=True)
    note = Column(Boolean, default=True)
    task = Column(Boolean, default=True)
    reminder = Column(Boolean, default=True)
    email = Column(Boolean, default=True)
    push = Column(Boolean, default=False)
    user_id = Column(String, ForeignKey("user.id"),  unique=True)


class Session(Base):
    __tablename__ = "session"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("user.id"),  unique=True, index=True)
    access_token = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=now())
    end_at = Column(TIMESTAMP)


class Note(Base):
    __tablename__ = "notes"
    id = Column(String, primary_key=True)
    tweet_id = Column(String)
    user_id = Column(String, ForeignKey("user.id"),  unique=True, index=True)
    content = Column(String)
    created_at = Column(TIMESTAMP, server_default=now())


class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(String, primary_key=True)
    tweet_id = Column(String)
    user_id = Column(String, ForeignKey("user.id"),  unique=True, index=True)
    content = Column(String)
    date = Column(DateTime)
    created_at = Column(TIMESTAMP, server_default=now())


class Tasklist(Base):
    __tablename__ = "tasklists"
    id = Column(String, primary_key=True)
    tweet_id = Column(String)
    user_id = Column(String, ForeignKey("user.id"),  unique=True, index=True)
    content = Column(String)
    created_at = Column(TIMESTAMP, server_default=now())
    tasks = relationship("Task", backref="tasklists", lazy='joined')
    

class Task(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True)
    tasklist_id = Column(String, ForeignKey("tasklists.id"),  unique=True, index=True)
    complete = bool
    content = Column(String)