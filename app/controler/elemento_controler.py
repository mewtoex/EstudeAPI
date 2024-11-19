import os
from flask import jsonify, request
from controler.elemento.query_builder import save_elemento, update_elemento, elemento_list

def elemento_list_get():  
    results = elemento_list()

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de elemento"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def save_controller_elemento():  
    data = request.get_json()
    elemento = data.get('elemento')
    results = save_elemento(elemento)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "elemento não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_elemento():  
    data = request.get_json()
    elemento = data.get('elemento')
    results = update_elemento(elemento)
    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "elemento não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500