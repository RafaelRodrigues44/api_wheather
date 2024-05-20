# mongo_utils.py

from pymongo import MongoClient
from django.conf import settings

def get_mongo_db():
    connection_string = settings.DMONGODB_DATABASES
    database_name = settings.MONGO_DATABASE_NAME
    client = MongoClient(connection_string)
    db = client[database_name]
    return db
