import os
from flask import jsonify, request
from controler.pivete.query_builder import insert_pivete,busca_pivete_por_user,alterar_pivete

def busca_pivete_por_user():  
    data = request.get_json()
    id_user = data.get('idUser')
    results = busca_pivete_por_user(id_user)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de pivete"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def save_controller_pivete():  
    data = request.get_json()
    pivete = data.get('pivete')

    results = insert_pivete(pivete)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "pivete não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_pivete():  
    data = request.get_json()
    pivete = data.get('pivete')

    results = alterar_pivete(pivete)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "pivete não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500