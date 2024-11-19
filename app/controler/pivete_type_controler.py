import os
from flask import jsonify, request
from controler.pivete_type.query_builder import save_pivete_type, update_pivete_type, pivete_type_list

def pivete_type_list_get():  
    results = pivete_type_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de pivete_type"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
       
def save_controller_pivete_type():  
    data = request.get_json()
    pivete_type = data.get('pivete_type')
    results = save_pivete_type(pivete_type)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "pivete_type não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_pivete_type():  
    data = request.get_json()
    pivete_type = data.get('pivete_type')
    results = update_pivete_type(pivete_type)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "pivete_type não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500