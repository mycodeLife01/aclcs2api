from fastapi import FastAPI
from app.api.v1 import external
from .core.exception_handlers import register_exception_handlers

app = FastAPI(title="ACL CS2 External API", version="0.0.1")
app.include_router(external.router)
register_exception_handlers(app)
