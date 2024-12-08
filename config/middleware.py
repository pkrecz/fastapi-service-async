from typing import Callable, Awaitable
from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from .session import set_db_session_context, AsyncScopedSession


class SessionDBMiddleware(BaseHTTPMiddleware):

    async def dispatch(
                        self,
                        request: Request,
                        call_next: Callable[[Request],Awaitable[Response]]) -> Response:
        response = Response("Internal server error.", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            set_db_session_context(session_id=hash(request))
            response = await call_next(request)
        finally:
            await AsyncScopedSession.remove()
            set_db_session_context(session_id=None)
        return response
