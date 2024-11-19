import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def pecas_list():
    response = supabase.table('pecas').select("*").execute()
    return response.data
    
def save_pecas(pecas):
    supabase.table('pecas').insert(vars(pecas)).execute()

def update_pecas(pecas):
    supabase.table('pecas').update(vars(pecas)).eq('id', pecas.id).execute()


def pecas_list_type(id):
    response = supabase.table('pecas').select("*").or_('cria_type.eq.' + str(id) + ',cria_type.is.null').execute()
    return response.data

