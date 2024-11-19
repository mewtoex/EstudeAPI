import os
from flask import jsonify, request
from controler.poderes.query_builder import save_poderes, update_poderes, poderes_list, poderes_list_type

def poderes_list_get():  
    results = poderes_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de poderes"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def poderes_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = poderes_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de poderes"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_poderes():  
    data = request.get_json()
    poderes = data.get('poderes')
    results = save_poderes(poderes)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "poderes não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_poderes():  
    data = request.get_json()
    poderes = data.get('poderes')
    results = update_poderes(poderes)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "poderes não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500