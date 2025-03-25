import pandas as pd
from pymongo import MongoClient

# 1. Conectar ao MongoDB Atlas
username = "iglmacedo"
password = "D69tGgpgOvww99L6"  # Substitua pela sua senha
cluster_url = "anxiety-depression.g1qe1.mongodb.net"
database_name = "Anxiety-Depression"  # Substitua pelo nome do seu banco de dados
collection_name = "minha_colecao"  # Substitua pelo nome da sua coleção

# Montar a string de conexão
connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName={database_name}"

# Conectar ao MongoDB
client = MongoClient(connection_string)
db = client[database_name]
collection = db[collection_name]

# 2. Ler os dados do MongoDB e carregar em um DataFrame do Pandas
data = list(collection.find())  # Recupera todos os documentos da coleção
df = pd.DataFrame(data)  # Converte para DataFrame

# 3. Selecionar e reordenar as colunas desejadas
columns_to_export = [
    "Age",
    "Gender",
    "Education_Level",
    "Employment_Status",
    "Sleep_Hours",
    "Anxiety_Score",
    "Depression_Score",
    "Family_History_Mental_Illness",
    "Medication_Use",
    "Stress_Level",
    "Physical_Activity_Hrs",
    "Substance_Use",
    "Financial_Stress"
]

# Verificar se todas as colunas desejadas existem no DataFrame
for column in columns_to_export:
    if column not in df.columns:
        raise ValueError(f"A coluna '{column}' não existe no DataFrame.")

# Selecionar apenas as colunas desejadas
df = df[columns_to_export]

# 4. Aplicar transformações e limpeza nos dados
# - Preencher valores nulos em colunas numéricas com a média
numeric_columns = df.select_dtypes(include=["number"]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# - Preencher valores nulos em colunas de texto com "Unknown"
text_columns = df.select_dtypes(include=["object"]).columns
df[text_columns] = df[text_columns].fillna("Unknown")

# - Converter colunas de texto para maiúsculas
df[text_columns] = df[text_columns].apply(lambda x: x.str.upper())

# 5. Salvar o DataFrame em um arquivo CSV
print(df.head)
output_csv_path = r"C:\Users\igl_m\Downloads\mental_health_cleaned.csv"  # Substitua pelo caminho desejado
df.to_csv(output_csv_path, index=False)

print(f"Dados limpos e transformados salvos em: {output_csv_path}")