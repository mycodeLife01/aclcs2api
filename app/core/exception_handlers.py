from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .exceptions import DataNotFoundException


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(DataNotFoundException)
    async def data_not_found_exception_handler(
        request: Request, exc: DataNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": "DataNotFoundException",
                "param": exc.param,
                "message": exc.message,
            },
        )
