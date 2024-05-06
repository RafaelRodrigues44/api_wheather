from pymongo import MongoClient

def test_mongodb_connection():
    # Substitua as informações de conexão com suas próprias credenciais e detalhes do banco de dados
    client = MongoClient('mongodb+srv://gkrcido:abcd123@cluster0.xglpozx.mongodb.net/')
    
    try:
        # Teste de ping para verificar a conexão
        client.admin.command('ping')
        print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Falha na conexão: {e}")
    finally:
        # Feche a conexão
        client.close()

if __name__ == "__main__":
    test_mongodb_connection()
