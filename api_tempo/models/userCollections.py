from pymongo import MongoClient
from django.conf import settings

class CustomUserManagerMongoDB:
    def __init__(self):
        mongo_settings = settings.MONGODB_DATABASES['default']
        mongo_uri = f"mongodb+srv://{mongo_settings['USER']}:{mongo_settings['PASSWORD']}@{mongo_settings['HOST']}/{mongo_settings['NAME']}"
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_settings['NAME']]

    def get_collection(self):
        return self.db['custom_users']

    def insert_user(self, user_data):
        collection = self.get_collection()
        collection.insert_one(user_data)

    def find_user_by_email(self, email):
        collection = self.get_collection()
        return collection.find_one({'email': email})
