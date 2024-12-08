from contextvars import ContextVar
from typing import Optional
from sqlalchemy.ext.asyncio import async_sessionmaker, async_scoped_session, AsyncSession
from .database import engine


db_session_context: ContextVar[Optional[int]] = ContextVar("db_session_context", default=None)
local_session = async_sessionmaker(
                                    bind=engine,
                                    autoflush=False,
                                    autocommit=False)


def get_db_session_context():
    session_id = db_session_context.get()
    if not session_id:
        raise ValueError("Currently no session is available.")
    return int(session_id)


def set_db_session_context(*, session_id: int):
    db_session_context.set(session_id)


AsyncScopedSession = async_scoped_session(
                                            session_factory=local_session,
                                            scopefunc=get_db_session_context)


def get_current_session() -> AsyncSession:
    return AsyncScopedSession()
