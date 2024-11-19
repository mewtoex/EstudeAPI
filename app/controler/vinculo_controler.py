import os
from flask import jsonify, request
from controler.vinculo.query_builder import save_vinculo, update_vinculo, vinculo_list, vinculo_list_type

def vinculo_list_get():  
    results = vinculo_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de vinculo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def vinculo_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = vinculo_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de vinculo"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_vinculo():  
    data = request.get_json()
    vinculo = data.get('vinculo')
    results = save_vinculo(vinculo)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "vinculo não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_vinculo():  
    data = request.get_json()
    vinculo = data.get('vinculo')
    results = update_vinculo(vinculo)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "vinculo não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500