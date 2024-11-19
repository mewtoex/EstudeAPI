import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db import connect_to_db


supabase = connect_to_db()


def busca_cria_por_pivete(pivete_id):
    response = supabase.table('pivete').select('cria_id').eq('id', pivete_id).single().execute()
    cria_id = response.data['cria_id'] 

    cria_response = supabase.table('cria').select('*').eq('id', cria_id).single().execute()
    return cria_response.data

def busca_relacoes_por_cria(cria_id):
    response = supabase.table('cria_relacao').select('*').eq('cria_id', cria_id).execute()
    return response.data


def busca_cria_com_relacoes(pivete_id):
    cria = busca_cria_por_pivete(pivete_id)
    relacoes = busca_relacoes_por_cria(cria['id'])
    return {
        'cria': cria,
        'relacoes': relacoes
    }


def insert_cria(cria, pecas_ids, tecnicas_ids):
    cria_data = {
        'nome': cria['nome'],
        'durabilidade': cria['durabilidade'],
        'dano': cria['dano'],
        'mira': cria['mira'],
        'velocidade': cria['velocidade'],
        'carapaca': cria['carapaca'],
        'bateria': cria['bateria'],
        'elemento': cria['elemento'],
        'personalidade': cria['personalidade'],
        'memoria': cria['memoria'],
        'chassi': cria['chassi'],
        'status': cria['status'],
        'lado': cria['lado']
    }

    cria_response = supabase.table('cria').insert(cria_data).execute()
    if cria_response.status_code == 201:
        cria_id = cria_response.data[0]['id']

        for peca_id in pecas_ids:
            cria_peca_data = {
                'cria_id': cria_id,
                'peca_id': peca_id
            }
            supabase.table('CriaPeca').insert(cria_peca_data).execute()

        for tecnica_id in tecnicas_ids:
            cria_tecnica_data = {
                'cria_id': cria_id,
                'tecnica_id': tecnica_id
            }
            supabase.table('CriaTecnica').insert(cria_tecnica_data).execute()
        
        return (f"Cria inserida com sucesso! ID: {cria_id}")

    else:
        return("Erro ao inserir a Cria:", cria_response.error_message)


def update_cria(cria, pecas_ids, tecnicas_ids):
    cria_data = {
        'durabilidade': cria['durabilidade'],
        'dano': cria['dano'],
        'mira': cria['mira'],
        'velocidade': cria['velocidade'],
        'carapaca': cria['carapaca'],
        'bateria': cria['bateria'],
        'memoria': cria['memoria'],
        'status': cria['status'],
        'lado': cria['lado']
    }

    update_response = supabase.table('cria').update(cria_data).eq('id', cria['id']).execute()
    if update_response.status_code == 200:

        supabase.table('CriaPeca').delete().eq('cria_id', cria['id']).execute()
        for peca_id in pecas_ids:
            cria_peca_data = {
                'cria_id': cria['id'],
                'peca_id': peca_id
            }
            supabase.table('CriaPeca').insert(cria_peca_data).execute()

        supabase.table('CriaTecnica').delete().eq('cria_id', cria['id']).execute()
        for tecnica_id in tecnicas_ids:
            cria_tecnica_data = {
                'cria_id': cria['id'],
                'tecnica_id': tecnica_id
            }
            supabase.table('CriaTecnica').insert(cria_tecnica_data).execute()
        return (f"Cria atualizada com sucesso! ID: {cria['id']}")

    else:
        return("Erro ao atualizar a Cria:", update_response.error_message)




pecas_ids = [1, 2, 3]  
tecnicas_ids = [1, 4, 5]  