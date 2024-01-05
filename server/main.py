import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from server.api.webs import router as webs_router
from server.constants.base import RESOURSE_UNAVAILABLE
from server.exceptions.base import CustomHTTPException
from server.settings import get_settings

settings = get_settings()


app = FastAPI(
    title="Goss Practice",
)
logger = logging.getLogger("main")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webs_router, tags=["webs"])


@app.middleware("http")
async def error_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        error_message = f"Случилась ошибка: {str(exc)}"
        logger.exception(error_message)

        return JSONResponse(
            status_code=500,
            content={"detail": {"msg": RESOURSE_UNAVAILABLE}},
        )


@app.exception_handler(CustomHTTPException)
async def exception_handler(request: Request, exc: CustomHTTPException):
    detail = exc.detail
    status_code = exc.status_code
    logger.exception(detail)

    return JSONResponse(
        status_code=status_code,
        content={"detail": detail},
    )


def main():
    uvicorn.run(
        "server.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=True,
    )


if __name__ == "__main__":
    main()
