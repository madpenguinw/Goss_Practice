import certifi
from motor import motor_asyncio

from server.settings import get_settings

settings = get_settings()

client = motor_asyncio.AsyncIOMotorClient(
    settings.db_dsn, tlsCAFile=certifi.where()
)
db = client[settings.MONGO_DB_NAME]
