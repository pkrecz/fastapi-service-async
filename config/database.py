import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base


url = os.getenv("DATABASE_URL")

engine = create_async_engine(url, pool_size=100, max_overflow=0, pool_pre_ping=False)
Base = declarative_base()
