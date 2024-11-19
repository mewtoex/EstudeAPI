import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def personalidade_list():
    response = supabase.table('personalidade').select("*").execute()
    return response.data
    
def save_personalidade(personalidade):
    supabase.table('personalidade').insert(vars(personalidade)).execute()

def update_personalidade(personalidade):
    supabase.table('personalidade').update(vars(personalidade)).eq('id', personalidade.id).execute()
