import os
from flask import jsonify, request
from controler.especial.query_builder import save_especial, update_especial, especial_list, especial_list_type

def especial_list_get():  
    results = especial_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de especial"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


def especial_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = especial_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de vinculo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def save_controller_especial():  
    data = request.get_json()
    especial = data.get('especial')
    results = save_especial(especial)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "especial não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_especial():  
    data = request.get_json()
    especial = data.get('especial')
    results = update_especial(especial)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "especial não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500