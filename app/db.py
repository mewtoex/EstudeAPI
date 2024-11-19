from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

print(f"SUPABASE_URL: {SUPABASE_URL}")
print(f"SUPABASE_KEY: {SUPABASE_KEY}")

def connect_to_db():
    try:
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise ValueError("SUPABASE_URL ou SUPABASE_KEY não estão definidos.")
        
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        if supabase is None:
            raise Exception("Falha ao criar o cliente Supabase.")
        
        print("Cliente Supabase criado com sucesso.")
        return supabase
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return None

supabase = connect_to_db()
if supabase:
    print("Conexão com o Supabase estabelecida com sucesso.")
else:
    print("Falha na conexão com o Supabase.")
