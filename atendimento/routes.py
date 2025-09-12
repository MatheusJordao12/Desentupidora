from flask import Blueprint, jsonify, request
from .models import OS

atendimento_bp = Blueprint('atendimento', __name__)

# Lista de ordens de serviço simulada
ORDENS = []

@atendimento_bp.route('/os', methods=['GET'])
def listar_os():
    """Retorna todas as ordens de serviço"""
    return jsonify(ORDENS)

@atendimento_bp.route('/os', methods=['POST'])
def criar_os():
    """Cria uma nova ordem de serviço"""
    data = request.get_json()
    os_id = len(ORDENS) + 1
    nova_os = {
        'id': os_id,
        'cliente': data.get('cliente'),
        'servico': data.get('servico'),
        'status': 'Pendente',
        'historico': []
    }
    ORDENS.append(nova_os)
    return jsonify(nova_os), 201

@atendimento_bp.route('/os/<int:os_id>', methods=['PUT'])
def atualizar_os(os_id):
    """Atualiza status ou histórico de uma OS"""
    os_item = next((o for o in ORDENS if o['id'] == os_id), None)
    if not os_item:
        return jsonify({'error': 'OS não encontrada'}), 404
    data = request.get_json()
    os_item['status'] = data.get('status', os_item['status'])
    if 'historico' in data:
        os_item['historico'].append(data['historico'])
    return jsonify(os_item)
