from datetime import datetime
from typing import Any

from bson.objectid import ObjectId
from fastapi import APIRouter
from fastapi_restful.cbv import cbv

from server.conections.base import collection
from server.constants.base import FORMAT
from server.exceptions.webs import WebNotFoundException
from server.schemas.webs import ShortWebOut, ShortWebOutList, WebIn, WebOut
from server.schemas.terms import Term
from server.schemas.links import Link
from server.settings import get_settings
from http import HTTPStatus


router = APIRouter()
settings = get_settings()


@cbv(router)
class WebsAPI:
    """
    Webs API endpoints
    """
    
    @router.get("/web/")
    async def get_all_webs(self) -> ShortWebOutList:
        """
        Get a short information about all webs from the MongoDB
        """
        cursor = collection.find({}, {"_id": 1, "name": 1})
        result_values = []
        async for document in cursor:
            _id = document.get("_id")
            name = document.get("name")
            if _id and name:
                result_values.append(
                    ShortWebOut(
                        id=str(_id),
                        name=name
                    )
                )
        return ShortWebOutList(values=result_values)

    @router.get("/web/{id}")
    async def get_web(self, _id: str) -> WebOut:
        """
        Get a full web information from the MongoDB
        """
        web = await collection.find_one({"_id": ObjectId(_id)})
        terms = web["terms"]
        links = web["links"]
        return WebOut(
            id=str(web["_id"]),
            name=web["name"],
            author=web["author"],
            created=web["created"],
            terms=[
                Term(
                    id=term["id"],
                    name=term["name"],
                    description=term["description"],
                )
                for term in terms
            ],
            links=[
                Link(
                    name=link["name"],
                    from_term=link["from_term"],
                    to_term=link["to_term"],
                )
                for link in links
            ],
        )

    @router.post("/web", status_code=HTTPStatus.CREATED)
    async def create_web(
        self,
        web_in: WebIn,
    ) -> ShortWebOut:
        """
        Create a web and save it to MongoDB
        """
        created = datetime.utcnow().strftime(FORMAT)
        terms = web_in.terms
        links = web_in.links
        web_dict = dict(
            name=web_in.name,
            author=web_in.author,
            created=created,
            terms=[dict(id=term.id, name=term.name, description=term.description) for term in terms],
            links=[dict(from_term=link.from_term, name=link.name, to_term=link.to_term) for link in links]
        )
        inserted_web = await collection.insert_one(web_dict)
        print(type(inserted_web.inserted_id))
        return ShortWebOut(
            id=str(inserted_web.inserted_id),
            name=web_in.name,
        )

    @router.delete("/web/{id}", status_code=HTTPStatus.NO_CONTENT)
    async def delete_web(self, _id: str) -> None:
        """
        Delete a web from MongoDB
        """
        result = await collection.delete_one({"_id": ObjectId(_id)})
        deleted_count = result.deleted_count
        if not deleted_count:
            raise WebNotFoundException(web_id=_id)
        return
