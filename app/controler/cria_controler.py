import os
from flask import jsonify, request
from controler.cria.query_builder import update_cria,busca_cria_com_relacoes,insert_cria

def busca_cria_com_relacoes():  
    data = request.get_json()
    id_pivete = data.get('idPivete')
    results = busca_cria_com_relacoes(id_pivete)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "Erro ao buscar lista de cria"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

def save_controller_cria():  
    data = request.get_json()
    cria = data.get('cria')
    pecas = data.get('pecas')
    tecnica = data.get('tecnica')

    results = insert_cria(cria,pecas,tecnica)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "cria não salvo."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
def update_controller_cria():  
    data = request.get_json()
    cria = data.get('cria')
    pecas = data.get('pecas')
    tecnica = data.get('tecnica')

    results = update_cria(cria,pecas,tecnica)

    try:
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": "cria não atualizado."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500