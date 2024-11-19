import os 
from flask import request, jsonify
import jwt
from functools import wraps

SECRET_KEY = os.getenv('SUPABASE_KEY')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if token and token.startswith('Bearer '):
            token = token.split(' ')[1]  
        else:
            token = None  
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            print("Decoded JWT data:", data)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403
        except Exception as e:
            print("Error decoding token:", str(e))
            return jsonify({'message': 'Token is invalid!'}), 403

        if 'user_id' not in data:
            return jsonify({'message': 'Token does not contain user_id!'}), 403

        return f(data['user_id'], *args, **kwargs)

    return decorated
