from django.conf import settings
import pymongo
from bson import ObjectId
from django.contrib.auth.hashers import check_password
 
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
    
    def get_by_email(self, email=None):
        query = {}
        if email:
            query['email'] = email
        
        documents = self.get_collection().find(query)
        return list(documents)
   
    def create_user(self, user_data):
        collection = self.get_collection()
        result = collection.insert_one(user_data)
        return result.inserted_id
   
    def delete(self, document_id):
        self.get_collection().delete_one({'_id': ObjectId(document_id)})

    def update(self, document_id, new_user_data):
        self.get_collection().update_one({'_id': ObjectId(document_id)}, {'$set': new_user_data})

    def authenticate_user(self, email, password):
        user = self.get_by_email(email=email)
        
        if user:
            # Obter a senha armazenada do usuário no banco de dados
            stored_password = user[0]['password']
            print(password)
            print(stored_password)
            # Comparar a senha fornecida com a senha armazenada usando check_password
            if check_password(password, stored_password):
                return user[0]    
        return None
    
    def get(self, document_id):
     return self.get_collection().find_one({'_id': ObjectId(document_id)})
