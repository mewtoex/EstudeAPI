import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def especial_list():
    response = supabase.table('especial').select("*").execute()
    return response.data

def especial_list_type(id):
    response = supabase.table('especial').select("*").eq('privete_id', id).execute()
    return response.data

def save_especial(especial):
    supabase.table('personalidade').insert(vars(especial)).execute()

def update_especial(especial):
    supabase.table('especial').update(vars(especial)).eq('id', especial.id).execute()

