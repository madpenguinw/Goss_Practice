from server.exceptions.base import NotFoundException


class WebNotFoundException(NotFoundException):
    def __init__(
        self,
        web_id: str,
    ) -> None:
        msg = f"Запись в MongoDB c _id='{web_id}' не найдена"
        super().__init__(msg=msg)
