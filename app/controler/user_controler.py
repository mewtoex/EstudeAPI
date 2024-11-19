import os
import jwt
import datetime
from flask import jsonify, request
from controler.user.query_builder import login_bd, save_user, update_user
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SUPABASE_KEY')

def login_controller_user():  
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400

    results = login_bd(user, password)

    try:
        if results:
            token = jwt.encode({
                'user_id': results,  
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=240)  
            }, SECRET_KEY, algorithm='HS256')

            return jsonify({"token": token,'id': results }), 200
        else:
            return jsonify({"message": "Usuário ou senha inválidos."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_user():  
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400

    results = save_user(user, password)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Usuário não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_user():  
    data = request.get_json()
    user = data.get('user')
    password = data.get('pass')

    if not user or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios."}), 400

    results = update_user(user, password)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Usuário não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def generate_reset_code():
    return str(random.randint(100000, 999999))

def request_password_reset():
    data = request.get_json()
    user_email = data.get('email')
    
    if not user_email:
        return jsonify({"message": "O email é obrigatório."}), 400
    
    try:
        user = supabase.table('user').select('id').eq('email', user_email).execute()
        if not user.data:
            return jsonify({"message": "Usuário não encontrado."}), 404
        
        user_id = user.data[0]['id']
        reset_code = generate_reset_code()
        
        supabase.table('password_reset').insert({
            'user_id': user_id,
            'reset_code': reset_code
        }).execute()
        
        send_reset_code_to_user(user_email, reset_code)
        return jsonify({"message": "Código de reset enviado."}), 200
    
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def reset_password():
    data = request.get_json()
    reset_code = data.get('reset_code')
    new_password = data.get('new_password')
    
    if not reset_code or not new_password:
        return jsonify({"message": "Código de reset e nova senha são obrigatórios."}), 400
    
    try:
        reset_entry = supabase.table('password_reset').select('user_id').eq('reset_code', reset_code).eq('is_used', False).execute()
        if not reset_entry.data:
            return jsonify({"message": "Código inválido ou já utilizado."}), 400
        
        user_id = reset_entry.data[0]['user_id']
        
        hashed_password = hash_password(new_password)
        supabase.table('user').update({'senha': hashed_password.decode('utf-8')}).eq('id', user_id).execute()
        
        supabase.table('password_reset').update({'is_used': True}).eq('reset_code', reset_code).execute()
        
        return jsonify({"message": "Senha redefinida com sucesso."}), 200
    
    except Exception as e:
        return jsonify({"message": str(e)}), 500