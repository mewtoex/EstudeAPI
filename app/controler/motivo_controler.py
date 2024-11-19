import os
from flask import jsonify, request
from controler.motivo.query_builder import save_motivo, update_motivo, motivo_list, motivo_list_type

def motivo_list_get():  
    results = motivo_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de motivo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def motivo_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = motivo_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de motivo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_motivo():  
    data = request.get_json()
    motivo = data.get('motivo')
    results = save_motivo(motivo)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "motivo não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_motivo():  
    data = request.get_json()
    motivo = data.get('motivo')
    results = update_motivo(motivo)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "motivo não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500