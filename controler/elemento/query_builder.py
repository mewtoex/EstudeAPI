import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()

def elemento_list():
    response = supabase.table('elemento_cria').select("*").execute()
    return response.data
    
def save_elemento(elemento):
    supabase.table('elemento_cria').insert(vars(elemento)).execute()

def update_elemento(elemento):
    supabase.table('elemento_cria').update(vars(elemento)).eq('id', elemento.id).execute()

