from server.schemas.base import BaseForm


class Link(BaseForm):
    name: str
    from_term: int
    to_term: int
