import pandas as pd
from pymongo import MongoClient

# 1. Ler o arquivo CSV
csv_path = r"C:\Users\igl_m\Downloads\archive\anxiety_depression_data.csv"
df = pd.read_csv(csv_path)

# 2. Configurar a string de conexão do MongoDB Atlas
username = "iglmacedo"
password = "jIcMEvL245Smi97r"  # Substitua pela sua senha
cluster_url = "anxietydepressionmental.02yw0ss.mongodb.net"
database_name = "AnxietyDepression"  # Substitua pelo nome do seu banco de dados
collection_name = "DepressionAndAnxiety"  # Substitua pelo nome da sua coleção

# Montar a string de conexão
connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName={database_name}"

# 3. Conectar ao MongoDB Atlas
client = MongoClient(connection_string)
db = client[database_name]
collection = db[collection_name]

# 4. Converter o DataFrame para uma lista de dicionários
data = df.to_dict(orient="records")

# 5. Inserir os dados no MongoDB
collection.insert_many(data)

print("Dados inseridos com sucesso no MongoDB Atlas!")