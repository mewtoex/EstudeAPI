import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()

def chassi_list():
    response = supabase.table('chassi').select("*").execute()
    return response.data
    
def save_chassi(chassi):
    supabase.table('chassi').insert(vars(chassi)).execute()

def update_chassi(chassi):
    supabase.table('chassi').update(vars(chassi)).eq('id', chassi.id).execute()
