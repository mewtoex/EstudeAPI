import os
from flask import jsonify, request
from controler.quarto.query_builder import save_quarto, update_quarto, quarto_list, quarto_list_type

def quarto_list_get():  
    results = quarto_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de quarto"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def quarto_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = quarto_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de quarto"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_quarto():  
    data = request.get_json()
    quarto = data.get('quarto')
    results = save_quarto(quarto)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "quarto não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_quarto():  
    data = request.get_json()
    quarto = data.get('quarto')
    results = update_quarto(quarto)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "quarto não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500