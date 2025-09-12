from flask import Blueprint, jsonify, request
from .models import Material

estoque_bp = Blueprint('estoque', __name__)

MATERIAIS = []

@estoque_bp.route('/materiais', methods=['POST'])
def criar_material():
    """Adiciona material ao estoque"""
    data = request.get_json()
    id_mat = len(MATERIAIS)+1
    mat = Material(id_mat, data['nome'], data['quantidade'])
    MATERIAIS.append(mat)
    return jsonify({'id':mat.id,'nome':mat.nome,'quantidade':mat.quantidade}),201

@estoque_bp.route('/materiais/<int:id_mat>', methods=['PUT'])
def atualizar_material(id_mat):
    """Atualiza quantidade e histórico do material"""
    mat = next((m for m in MATERIAIS if m.id==id_mat), None)
    if not mat:
        return jsonify({'error':'Material não encontrado'}),404
    data = request.get_json()
    mat.historico.append({'quantidade': mat.quantidade, 'acao': data.get('acao','Atualização')})
    mat.quantidade = data.get('quantidade', mat.quantidade)
    return jsonify({'id':mat.id,'nome':mat.nome,'quantidade':mat.quantidade})
@estoque_bp.route('/materiais/<int:id_mat>/historico', methods=['GET'])
def historico_material(id_mat):
    """Retorna o histórico de movimentações do material"""
    mat = next((m for m in MATERIAIS if m.id==id_mat), None)
    if not mat:
        return jsonify({'error':'Material não encontrado'}),404
    return jsonify({'id':mat.id,'nome':mat.nome,'historico':mat.historico})
@estoque_bp.route('/materiais', methods=['GET'])
def listar_materiais():
    """Lista todos os materiais no estoque"""
    return jsonify([{'id':m.id,'nome':m.nome,'quantidade':m.quantidade} for m in MATERIAIS])