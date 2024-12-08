from functools import wraps
from typing import Callable, Awaitable, Any
from config.session import get_current_session


AsyncCallable = Callable[..., Awaitable]


def transactional(function: AsyncCallable) -> AsyncCallable:
    @wraps(function)
    async def wrap_function(*args, **kwargs) -> Awaitable[Any]:
        try:
            db_session = get_current_session()
            if db_session.in_transaction():
                return await function(*args, **kwargs)
            async with db_session.begin():
                result = await function(*args, **kwargs, db=db_session)
            return result
        except Exception as exception:
            raise
    return wrap_function
