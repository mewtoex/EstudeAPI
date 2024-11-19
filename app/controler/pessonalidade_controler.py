import os
from flask import jsonify, request
from controler.personalidade.query_builder import save_personalidade, update_personalidade, personalidade_list

def personalidade_list_get():  
    results = personalidade_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de personalidade"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
    
def save_controller_personalidade():  
    data = request.get_json()
    personalidade = data.get('personalidade')
    results = save_personalidade(personalidade)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "personalidade não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_personalidade():  
    data = request.get_json()
    personalidade = data.get('personalidade')
    results = update_personalidade(personalidade)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "personalidade não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500