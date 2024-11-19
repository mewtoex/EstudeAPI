import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def motivo_list():
    response = supabase.table('motivo').select("*").execute()
    return response.data

def motivo_list_type(id):
    response = supabase.table('motivo').select("*").eq('privete_id', id).execute()
    return response.data

def save_motivo(motivo):
    supabase.table('motivo').insert(vars(motivo)).execute()

def update_motivo(motivo):
    supabase.table('motivo').update(vars(motivo)).eq('id', motivo.id).execute()

