from flask import Blueprint
from flask_cors import CORS 
from app.controler.chassi_controler import chassi_list_get, save_controller_chassi, update_controller_chassi
from app.controler.cria_controler import busca_cria_com_relacoes, save_controller_cria, update_controller_cria
from app.controler.elemento_controler import elemento_list_get, save_controller_elemento, update_controller_elemento
from app.controler.especial_controler import especial_list_get, especial_list_get_type, save_controller_especial, update_controller_especial
from app.controler.fraquezas_type_controler import fraqueza_list_get, fraqueza_list_get_type, save_controller_fraqueza, update_controller_fraqueza
from app.controler.motivo_controler import motivo_list_get, motivo_list_get_type, save_controller_motivo, update_controller_motivo
from app.controler.objetivo_controler import objetivo_list_get, objetivo_list_get_type, save_controller_objetivo, update_controller_objetivo 
from app.controler.objeto_controler import objeto_list_get, objeto_list_get_type, save_controller_objeto, update_controller_objeto
from app.controler.pecas_controler import pecas_list_get, pecas_list_get_type, save_controller_pecas, update_controller_pecas
from app.controler.pessonalidade_controler import personalidade_list_get, save_controller_personalidade, update_controller_personalidade
from app.controler.pivete_controler import busca_pivete_por_user, save_controller_pivete, update_controller_pivete
from app.controler.pivete_type_controler import pivete_type_list_get, save_pivete_type, update_pivete_type
from app.controler.poderes_controler import poderes_list_get, poderes_list_get_type, save_controller_poderes, update_controller_poderes
from app.controler.quarto_controler import quarto_list_get, quarto_list_get_type, save_controller_quarto, update_controller_quarto
from app.controler.tecnicas_controler import tecnica_list_get, tecnica_list_get_filter, save_controller_tecnica,update_controller_tecnica
from app.controler.vinculo_controler import vinculo_list_get, vinculo_list_get_type, save_controller_vinculo, update_controller_vinculo
from app.controler.user_controler import login_controller_user, save_controller_user, update_controller_user
from app.decorators import token_required

api_blueprint = Blueprint('api', __name__)

CORS(api_blueprint, resources={r"/*": {"origins": "*"}})

#region User
@api_blueprint.route('/login', methods=['POST'])  
def login():
    return login_controller_user()

@api_blueprint.route('/user/new', methods=['POST'])
def save_user():
    return save_controller_user()

@api_blueprint.route('/user/update', methods=['POST']) 
@token_required 
def update_user():
    return update_controller_user()
#endregion

#region Vinculo
@api_blueprint.route('/vinculo/list', methods=['POST'])  
@token_required
def list_get_vinculos(user_id):
    return vinculo_list_get()

@api_blueprint.route('/vinculo/list_gettype', methods=['POST'])  
@token_required
def list_get_vinculo_types(user_id):
    return vinculo_list_get_type()

@api_blueprint.route('/vinculo/new', methods=['POST'])  
@token_required
def save_vinculo(user_id):
    return save_controller_vinculo()

@api_blueprint.route('/vinculo/update', methods=['POST'])  
@token_required
def update_vinculo(user_id):
    return update_controller_vinculo()
#endregion

#region Tecnica
@api_blueprint.route('/tecnica/list', methods=['POST']) 
@token_required 
def list_get_tecnicas(user_id):
    return tecnica_list_get()

@api_blueprint.route('/tecnica/tecnicatype', methods=['POST'])  
@token_required
def list_get_tecnica_types(user_id):
    return tecnica_list_get_filter()

@api_blueprint.route('/tecnica/new', methods=['POST'])  
@token_required
def save_tecnica(user_id):
    return save_controller_tecnica()

@api_blueprint.route('/tecnica/update', methods=['POST'])  
@token_required
def update_tecnica(user_id):
    return update_controller_tecnica()
#endregion

#region Quarto
@api_blueprint.route('/quarto/list', methods=['POST'])  
@token_required
def list_get_quartos(user_id):
    return quarto_list_get()

@api_blueprint.route('/quarto/list_gettype', methods=['POST'])  
@token_required
def list_get_quarto_types(user_id):
    return quarto_list_get_type()

@api_blueprint.route('/quarto/new', methods=['POST'])  
@token_required
def save_quarto(user_id):
    return save_controller_quarto()

@api_blueprint.route('/quarto/update', methods=['POST'])  
@token_required
def update_quarto(user_id):
    return update_controller_quarto()
#endregion

#region Poderes
@api_blueprint.route('/poderes/list', methods=['POST'])  
@token_required
def list_get_poderes(user_id):
    return poderes_list_get()

@api_blueprint.route('/poderes/list_gettype', methods=['POST'])  
@token_required
def list_get_poderes_types(user_id):
    return poderes_list_get_type()

@api_blueprint.route('/poderes/new', methods=['POST']) 
@token_required 
def save_poder(user_id):
    return save_controller_poderes()

@api_blueprint.route('/poderes/update', methods=['POST'])  
@token_required
def update_poder(user_id):
    return update_controller_poderes()
#endregion

#region Pivete type
@api_blueprint.route('/pivetetype/list', methods=['POST'])  
@token_required
def list_get_pivete_types(user_id):
    return pivete_type_list_get()

@api_blueprint.route('/pivetetype/new', methods=['POST'])  
@token_required
def save_pivete_type(user_id):
    return save_pivete_type()

@api_blueprint.route('/pivetetype/update', methods=['POST'])  
@token_required
def update_pivete_type(user_id):
    return update_pivete_type()
#endregion

#region Pivete
@api_blueprint.route('/pivete/list', methods=['POST'])  
@token_required
def list_get_pivetes(user_id):
    return busca_pivete_por_user() 

@api_blueprint.route('/pivete/new', methods=['POST'])  
@token_required
def save_pivete(user_id):
    return save_controller_pivete()

@api_blueprint.route('/pivete/update', methods=['POST'])  
@token_required
def update_pivete(user_id):
    return update_controller_pivete()
#endregion

#region Pessonalidade
@api_blueprint.route('/pessonalidade/list', methods=['POST'])  
@token_required
def list_get_personalidades(user_id):
    return personalidade_list_get()

@api_blueprint.route('/pessonalidade/new', methods=['POST'])  
@token_required
def save_personalidade(user_id):
    return save_controller_personalidade()

@api_blueprint.route('/pessonalidade/update', methods=['POST'])  
@token_required
def update_personalidade(user_id):
    return update_controller_personalidade()
#endregion

#region Pecas
@api_blueprint.route('/pecas/list', methods=['POST'])  
@token_required
def list_get_pecas(user_id):
    return pecas_list_get()

@api_blueprint.route('/pecas/list_gettype', methods=['POST'])  
@token_required
def list_get_pecas_types(user_id):
    return pecas_list_get_type()

@api_blueprint.route('/pecas/new', methods=['POST'])  
@token_required
def save_pecas(user_id):
    return save_controller_pecas()

@api_blueprint.route('/pecas/update', methods=['POST'])  
@token_required
def update_pecas(user_id):
    return update_controller_pecas()
#endregion

#region Objeto
@api_blueprint.route('/objeto/list', methods=['POST'])  
@token_required
def list_get_objetos(user_id):
    return objeto_list_get()

@api_blueprint.route('/objeto/list_gettype', methods=['POST'])  
@token_required
def list_get_objeto_types(user_id):
    return objeto_list_get_type()

@api_blueprint.route('/objeto/new', methods=['POST'])  
@token_required
def save_objeto(user_id):
    return save_controller_objeto()

@api_blueprint.route('/objeto/update', methods=['POST'])  
@token_required
def update_objeto(user_id):
    return update_controller_objeto()
#endregion

#region Objetivo
@api_blueprint.route('/objetivo/list', methods=['POST'])  
@token_required
def list_get_objetivos(user_id):
    return objetivo_list_get()

@api_blueprint.route('/objetivo/list_gettype', methods=['POST'])  
@token_required
def list_get_objetivo_types(user_id):
    return objetivo_list_get_type()

@api_blueprint.route('/objetivo/new', methods=['POST'])  
@token_required
def save_objetivo(user_id):
    return save_controller_objetivo()

@api_blueprint.route('/objetivo/update', methods=['POST'])  
@token_required
def update_objetivo(user_id):
    return update_controller_objetivo()
#endregion

#region Motivo
@api_blueprint.route('/motivo/list', methods=['POST'])  
@token_required
def list_get_motivos(user_id):
    return motivo_list_get()

@api_blueprint.route('/motivo/list_gettype', methods=['POST'])  
@token_required
def list_get_motivo_types(user_id):
    return motivo_list_get_type()

@api_blueprint.route('/motivo/new', methods=['POST'])  
@token_required
def save_motivo(user_id):
    return save_controller_motivo()

@api_blueprint.route('/motivo/update', methods=['POST'])  
@token_required
def update_motivo(user_id):
    return update_controller_motivo()
#endregion

#region Fraquezas
@api_blueprint.route('/fraquezas/list', methods=['POST'])  
@token_required
def list_get_fraquezas(user_id):
    return fraqueza_list_get()

@api_blueprint.route('/fraquezas/list_gettype', methods=['POST'])  
@token_required
def list_get_fraquezas_types(user_id):
    return fraqueza_list_get_type()

@api_blueprint.route('/fraquezas/new', methods=['POST'])  
@token_required
def save_fraqueza(user_id):
    return save_controller_fraqueza()

@api_blueprint.route('/fraquezas/update', methods=['POST'])  
@token_required
def update_fraqueza(user_id):
    return update_controller_fraqueza()
#endregion

#region Especial
@api_blueprint.route('/especial/list', methods=['POST'])  
@token_required
def list_get_especiais(user_id):
    return especial_list_get()

@api_blueprint.route('/especial/list_gettype', methods=['POST'])  
@token_required
def list_get_especial_types(user_id):
    return especial_list_get_type()

@api_blueprint.route('/especial/new', methods=['POST'])  
@token_required
def save_especial(user_id):
    return save_controller_especial()

@api_blueprint.route('/especial/update', methods=['POST'])  
@token_required
def update_especial(user_id):
    return update_controller_especial()
#endregion

#region Elemento
@api_blueprint.route('/elemento/list', methods=['POST'])  
@token_required
def list_get_elementos(user_id):
    return elemento_list_get()

@api_blueprint.route('/elemento/new', methods=['POST'])  
@token_required
def save_elemento(user_id):
    return save_controller_elemento()

@api_blueprint.route('/elemento/update', methods=['POST'])  
@token_required
def update_elemento(user_id):
    return update_controller_elemento()
#endregion

#region Cria
@api_blueprint.route('/cria/list', methods=['POST'])  
@token_required
def list_get_crias(user_id):
    return busca_cria_com_relacoes()

@api_blueprint.route('/cria/new', methods=['POST'])  
@token_required
def save_cria(user_id):
    return save_controller_cria()

@api_blueprint.route('/cria/update', methods=['POST'])  
@token_required
def update_cria(user_id):
    return update_controller_cria()
#endregion

#region Chassi
@api_blueprint.route('/chassi/list', methods=['POST'])  
@token_required
def list_get_chassis(user_id):
    return chassi_list_get()

@api_blueprint.route('/chassi/new', methods=['POST'])  
@token_required
def save_chassi(user_id):
    return save_controller_chassi()

@api_blueprint.route('/chassi/update', methods=['POST'])  
@token_required
def update_chassi(user_id):
    return update_controller_chassi()
#endregion
