import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def pivete_type_list():
    response = supabase.table('privete_type').select("*").execute()
    return response.data
    
def save_pivete_type(pivete_type):
    supabase.table('privete_type').insert(vars(pivete_type)).execute()

def update_pivete_type(pivete_type):
    supabase.table('privete_type').update(vars(pivete_type)).eq('id', pivete_type.id).execute()
