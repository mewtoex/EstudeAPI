import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()

def busca_pivete_por_user(user_id):
    response = supabase.table('pivete').select('*').eq('id_user', user_id).single().execute()
    return response.data

def insert_pivete(pivete):
    pivete_data = {
        'nome': pivete['nome'],
        'privete_type': pivete['privete_type'],
        'motivo_id': pivete['motivo_id'],
        'id_user': pivete['id_user'],
    }
    response =response =  supabase.table('privete').insert(pivete_data).execute()
    return response


def alterar_pivete(pivete):
    pivete_data = {
        'nome': pivete['nome'],
    }
    update_response = supabase.table('privete').update(pivete_data).eq('id', pivete['id']).execute()
    return update_response
