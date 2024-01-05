from http import HTTPStatus
from typing import Any

from fastapi import HTTPException


class CustomHTTPException(HTTPException):
    """
    Custom exception that modifies error response body
    Before:  {"detail": "Bad input"}
    After: {"detail": {"msg": "error"}}
    """

    status_code = HTTPStatus.BAD_REQUEST
    msg = "Произошла ошибка"

    def __init__(
        self,
        status_code: int | None = None,
        msg: str = "",
        headers: dict[str, Any] | None = None,
    ) -> None:
        status_code = status_code or self.status_code
        msg = msg or self.msg
        detail: dict[str, str] = {"msg": msg}
        super().__init__(status_code=status_code, detail=detail)
        self.headers = headers


class IncorrectInputData(CustomHTTPException):
    def __init__(self, msg=None):
        msg = msg if msg else "Введены некорректные данные"
        super().__init__(msg=msg)

    status_code = HTTPStatus.BAD_REQUEST


class NotFoundException(CustomHTTPException):
    msg = "Объект не найден"
    status_code = HTTPStatus.NOT_FOUND


class CustomNotFoundException(NotFoundException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg=msg, status_code=self.status_code)
