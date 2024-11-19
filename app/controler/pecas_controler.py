import os
from flask import jsonify, request
from controler.pecas.query_builder import save_pecas, update_pecas, pecas_list, pecas_list_type

def pecas_list_get():  
    results = pecas_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de pecas"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def pecas_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = pecas_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de pecas"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_pecas():  
    data = request.get_json()
    pecas = data.get('pecas')
    results = save_pecas(pecas)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "pecas não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_pecas():  
    data = request.get_json()
    pecas = data.get('pecas')
    results = update_pecas(pecas)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "pecas não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500