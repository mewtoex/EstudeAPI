import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def objeto_list():
    response = supabase.table('objeto').select("*").execute()
    return response.data

def objeto_list_type(id):
    response = supabase.table('objeto').select("*").eq('privete_id', id).execute()
    return response.data

def save_objeto(objeto):
    supabase.table('objeto').insert(vars(objeto)).execute()

def update_objeto(objeto):
    supabase.table('objeto').update(vars(objeto)).eq('id', objeto.id).execute()

