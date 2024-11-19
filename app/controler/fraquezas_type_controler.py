import os
from flask import jsonify, request
from controler.fraqueza.query_builder import save_fraqueza, update_fraqueza, fraqueza_list, fraqueza_list_type

def fraqueza_list_get():  
    results = fraqueza_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de fraqueza"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def fraqueza_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = fraqueza_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de fraqueza"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_fraqueza():  
    data = request.get_json()
    fraqueza = data.get('fraqueza')
    results = save_fraqueza(fraqueza)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "fraqueza não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_fraqueza():  
    data = request.get_json()
    fraqueza = data.get('fraqueza')
    results = update_fraqueza(fraqueza)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "fraqueza não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500