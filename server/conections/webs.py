from server.conections.base import db
from server.settings import get_settings

settings = get_settings()

collection = db[settings.MONGO_WEBS_COLLECTION]
