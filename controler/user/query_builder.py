import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db
from app.utils import hash_password, check_password

supabase = connect_to_db()

def user_exists(user):
    try:
        response = supabase.table('user').select("id").eq('login', user).execute()
        return len(response.data) > 0
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False
    
def login_bd(user, password):
    try:
        response = supabase.table('user').select("id", "senha").eq('login', user).execute()
        if response.data:
            stored_password_hash = response.data[0]['senha']
            id_user = response.data[0]['id']
            if check_password(password, stored_password_hash.encode('utf-8')): 
                return id_user
            else:
                return None
        return response.data
    except Exception as e:
        print(f"Erro ao fazer login: {e}")
        return None
    
def save_user(user, password):
    hashed_password = hash_password(password)
    try:
        supabase.table('user').insert({'login': user, 'senha': hashed_password.decode('utf-8')}).execute()
        return("Usuario salvo com sucesso!")
    except Exception as e:
        return(f"Erro ao salvar usuario: {e}")

def update_user(user, new_password):
    if not user_exists(user):
        return(f"Usuário {user} não existe.")
        return
    
    hashed_password = hash_password(new_password)
    try:
        supabase.table('user').update({'senha': hashed_password.decode('utf-8')}).eq('login', user).execute()
        return("Senha atualizada com sucesso!")
    except Exception as e:
        return(f"Erro ao atualizar a senha do usuário: {e}")
    