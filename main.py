import asyncio
from fastapi import FastAPI
from config.settings import settings
from config import registry


def start_application():
    app = FastAPI(
                    title=settings.title,
                    version=settings.version,
                    docs_url=settings.docs_url,
                    redoc_url=None,
                    contact={
                                "name": "Piotr",
                                "email": "pkrecz@poczta.onet.pl"})
    loop = asyncio.get_running_loop()
    loop.create_task(registry.create_tables())
    registry.load_routers(app)
    registry.load_middleware(app)
    return app

app = start_application()
