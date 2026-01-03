from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# SQLite URL for local development
# SQLALCHEMY_DATABASE_URL = 'sqlite:///todosapp.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
#                        'check_same_thread': False})

# PostgreSQL URL for production deployment

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:09127585948@localhost/TodoApplicationDatabase'

SQLALCHEMY_DATABASE_URL = 'postgresql://fastapi_todo_databse_user:FvNJenrA9WFg7akmvYHAjTAK7oIAmMz8@dpg-d5cfiiogjchc73cmkrc0-a.virginia-postgres.render.com/fastapi_todo_databse'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
