import os
from flask import jsonify, request
from controler.objetivo.query_builder import save_objetivo, update_objetivo, objetivo_list, objetivo_list_type

def objetivo_list_get():  
    results = objetivo_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de objetivo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def objetivo_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = objetivo_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de objetivo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_objetivo():  
    data = request.get_json()
    objetivo = data.get('objetivo')
    results = save_objetivo(objetivo)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "objetivo não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_objetivo():  
    data = request.get_json()
    objetivo = data.get('objetivo')
    results = update_objetivo(objetivo)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "objetivo não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500