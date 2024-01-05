from uuid import UUID

from server.schemas.base import BaseForm
from server.schemas.links import Link
from server.schemas.terms import Term


class WebIn(BaseForm):
    name: str
    author: str
    terms: list[Term]
    links: list[Link]


class WebOut(WebIn):
    id: str
    created: str


class ShortWebOut(BaseForm):
    id: str
    name: str


class ShortWebOutList(BaseForm):
    values: list[ShortWebOut]
