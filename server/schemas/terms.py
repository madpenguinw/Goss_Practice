from server.schemas.base import BaseForm


class Term(BaseForm):
    id: int
    name: str
    description: str
