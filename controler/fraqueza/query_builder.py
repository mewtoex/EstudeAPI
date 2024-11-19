import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def fraqueza_list():
    response = supabase.table('fraqueza').select("*").execute()
    return response.data

def fraqueza_list_type(id):
    response = supabase.table('fraqueza').select("*").eq('privete_id', id).execute()
    return response.data

def save_fraqueza(fraqueza):
    supabase.table('fraqueza').insert(vars(fraqueza)).execute()

def update_fraqueza(fraqueza):
    supabase.table('fraqueza').update(vars(fraqueza)).eq('id', fraqueza.id).execute()

