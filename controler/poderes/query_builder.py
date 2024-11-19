import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def poderes_list():
    response = supabase.table('poderes').select("*").execute()
    return response.data

def poderes_list_type(id):
    response = supabase.table('poderes').select("*").eq('privete_id', id).execute()
    return response.data

def save_poderes(poderes):
    supabase.table('poderes').insert(vars(poderes)).execute()

def update_poderes(poderes):
    supabase.table('poderes').update(vars(poderes)).eq('id', poderes.id).execute()
