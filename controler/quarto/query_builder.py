import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def quarto_list():
    response = supabase.table('quarto').select("*").execute()
    return response.data

def quarto_list_type(id):
    response = supabase.table('quarto').select("*").eq('privete_id', id).execute()
    return response.data

def save_quarto(quarto):
    supabase.table('quarto').insert(vars(quarto)).execute()

def update_quarto(quarto):
    supabase.table('quarto').update(vars(quarto)).eq('id', quarto.id).execute()
