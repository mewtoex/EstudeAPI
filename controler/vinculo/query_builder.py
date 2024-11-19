import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def vinculo_list():
    response = supabase.table('vinculo').select("*").execute()
    return response.data

def vinculo_list_type(id):
    response = supabase.table('vinculo').select("*").eq('privete_id', id).execute()
    return response.data

def save_vinculo(vinculo):
    supabase.table('vinculo').insert(vars(vinculo)).execute()

def update_vinculo(vinculo):
    supabase.table('vinculo').update(vars(vinculo)).eq('id', vinculo.id).execute()
