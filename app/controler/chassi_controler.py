import os
from flask import jsonify, request
from controler.chassi.query_builder import save_chassi, update_chassi, chassi_list

def chassi_list_get():  
    results = chassi_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de chassi"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_chassi():  
    data = request.get_json()
    chassi = data.get('chassi')
    results = save_chassi(chassi)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Chassi não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_chassi():  
    data = request.get_json()
    chassi = data.get('chassi')
    results = update_chassi(chassi)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Chassi não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500