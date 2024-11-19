import os
from flask import jsonify, request
from controler.tecnica.query_builder import save_tecnica, update_tecnica, tecnica_list, tecnica_list_filter

def tecnica_list_get():  
    results = tecnica_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de tecnica"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def tecnica_list_get_filter():  
    data = request.get_json()
    _filter = data.get('filter')
    results = tecnica_list_filter(_filter)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de tecnica"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_tecnica():  
    data = request.get_json()
    tecnica = data.get('tecnica')
    results = save_tecnica(tecnica)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "tecnica não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_tecnica():  
    data = request.get_json()
    tecnica = data.get('tecnica')
    results = update_tecnica(tecnica)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "tecnica não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500