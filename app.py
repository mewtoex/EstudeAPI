from flask import Flask, jsonify, request
import pyodbc
from pivete.query_builder import query, query1, query2
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()  

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

app = Flask(__name__)

def connect_to_db():
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return supabase
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return None

# Rota exemplo para executar uma query
@app.route('/execute-query', methods=['POST'])
def execute_query():
    query = request.json.get('query')
    conn = connect_to_db()
    if conn:
        try:
            results = pivete.query_builder.query1(2)
            return jsonify(results)
        except Exception as e:
            return jsonify({"message": f"Erro ao executar a query: {e}"}), 400
    else:
        return jsonify({"message": "Falha na conexão."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)