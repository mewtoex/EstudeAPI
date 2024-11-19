import os
from flask import jsonify, request
from controler.objeto.query_builder import save_objeto, update_objeto, objeto_list, objeto_list_type

def objeto_list_get():  
    results = objeto_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de objeto"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def objeto_list_get_type():  
    data = request.get_json()
    type_cria = data.get('idType')
    results = objeto_list_type(type_cria)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de objeto"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_objeto():  
    data = request.get_json()
    objeto = data.get('objeto')
    results = save_objeto(objeto)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "objeto não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_objeto():  
    data = request.get_json()
    objeto = data.get('objeto')
    results = update_objeto(objeto)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "objeto não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500