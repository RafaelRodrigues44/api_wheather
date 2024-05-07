from django.conf import settings
import pymongo
 
class UserRepository:
    collection_name = 'users'
 
    def __init__(self) -> None:
        self.collection_name = 'users'
 
    def get_collection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        db = client[getattr(settings, "MONGO_DATABASE_NAME")]
        collection = db[self.collection_name]
        return collection
   
    def get_all_users(self):
        collection = self.get_collection()
        users = collection.find({})
        return list(users)
   
    def get_user_by_email(self, email):
        collection = self.get_collection()
        user = collection.find_one({"email": email})
        return user
   
    def create_user(self, user_data):
        collection = self.get_collection()
        result = collection.insert_one(user_data)
        return result.inserted_id
 
    def check_password(self, user_email, entered_password):
        collection = self.get_collection()
        user = collection.find_one({"email": user_email})
 
        if user and user.get('password'):
            return user['password'] == entered_password
        return False
 
    def update_user(self, email, update_data):
        collection = self.get_collection()
        result = collection.update_one({"email": email}, {"$set": update_data})
        return result.modified_count
   
    def delete_user(self, email):
        collection = self.get_collection()
        result = collection.delete_one({"email": email})
        return result.deleted_count
   
    def authenticate_user(self, email, password):
        user = self.get_user_by_email(email)
        if user and self.check_password(password, user.get('password', '')):
            return True, user
        else:
            return False, None  