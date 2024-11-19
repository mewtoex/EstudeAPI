import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()

def tecnica_list():
    response = supabase.table('tecnica').select("*").execute()
    return response.data
    
def save_tecnica(tecnica):
    supabase.table('tecnica').insert(vars(tecnica)).execute()

def update_tecnica(tecnica):
    supabase.table('tecnica').update(vars(tecnica)).eq('id', tecnica.id).execute()

def tecnica_list_filter(pre):
    query = supabase.table('tecnicas').select("*")
    if not isinstance(pre, dict):
        return []
 
    if 'chassi' in pre and pre['chassi']:
        chassi = pre['chassi']
        query = query.or_(
            f"chassi.like.%{chassi}%,chassi.is.null"
        )
    if 'elemento' in pre and pre['elemento']:
        elemento = pre['elemento']
        query = query.or_(
            f"elemento.like.%{elemento}%,elemento.is.null"
        )
    if 'rank' in pre and pre['rank']:
        rank = pre['rank']
        query = query.or_(
            f"rank.like.%{rank}%,rank.is.null"
        )

    query = query.or_("prerequisito.eq.0")

    response = query.execute()

    return response.data if response.data else []

