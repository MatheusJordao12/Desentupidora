from flask import Blueprint, jsonify, request
from .models import Cliente, Orçamento

vendas_bp = Blueprint('vendas', __name__)

CLIENTES = []
ORCAMENTOS = []

@vendas_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.get_json()
    cliente_id = len(CLIENTES)+1
    cliente = Cliente(cliente_id, data['nome'], data['email'])
    CLIENTES.append(cliente)
    return jsonify({'id':cliente.id,'nome':cliente.nome,'email':cliente.email}),201

@vendas_bp.route('/orcamentos', methods=['POST'])
def criar_orcamento():
    data = request.get_json()
    id_orc = len(ORCAMENTOS)+1
    orc = Orçamento(id_orc, data['cliente_id'], data['servico'], data['valor'])
    ORCAMENTOS.append(orc)
    return jsonify({'id':orc.id,'cliente_id':orc.cliente_id,'servico':orc.servico,'valor':orc.valor}),201

@vendas_bp.route('/orcamentos/<int:id_orc>', methods=['PUT'])
def atualizar_orcamento(id_orc):
    orc = next((o for o in ORCAMENTOS if o.id==id_orc), None)
    if not orc:
        return jsonify({'error':'Orçamento não encontrado'}),404
    data = request.get_json()
    orc.status = data.get('status', orc.status)
    return jsonify({'id':orc.id,'status':orc.status})
