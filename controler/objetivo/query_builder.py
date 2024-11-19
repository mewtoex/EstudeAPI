import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def objetivo_list():
    response = supabase.table('objetivo').select("*").execute()
    return response.data

def objetivo_list_type(id):
    response = supabase.table('objetivo').select("*").eq('privete_id', id).execute()
    return response.data

def save_objetivo(objetivo):
    supabase.table('objetivo').insert(vars(objetivo)).execute()

def update_objetivo(objetivo):
    supabase.table('objetivo').update(vars(objetivo)).eq('id', objetivo.id).execute()

