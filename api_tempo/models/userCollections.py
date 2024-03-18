from pymongo import MongoClient
from django.conf import settings

class CustomUserManagerMongoDB:
    def __init__(self):
        # Configuração da conexão com o MongoDB Atlas
        mongo_uri = "mongodb+srv://gkrcido:128Acido@cluster0.xglpozx.mongodb.net/<database>?retryWrites=true&w=majority"
        
        # Inicializando o cliente MongoDB
        self.client = MongoClient(mongo_uri)
        
        # Acessando o banco de dados específico
        self.db = self.client['weather_rafaelRodrigues']
        
    def get_collection(self):
        # Obtendo a coleção desejada
        return self.db['custom_users']

    def insert_user(self, user_data):
        # Inserindo um usuário na coleção
        collection = self.get_collection()
        collection.insert_one(user_data)

    def find_user_by_email(self, email):
        # Procurando um usuário pelo email na coleção
        collection = self.get_collection()
        return collection.find_one({'email': email})
    
    def __del__(self):
        # Fechando a conexão com o MongoDB quando a instância for destruída
        if self.client:
            self.client.close()
