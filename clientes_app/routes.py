from flask import Blueprint, jsonify, request
from .models import Solicitacao, PagamentoApp

clientes_bp = Blueprint('clientes', __name__)

SOLICITACOES = []
PAGAMENTOS_APP = []

@clientes_bp.route('/solicitacoes', methods=['POST'])
def nova_solicitacao():
    """Cria solicitação do cliente"""
    data = request.get_json()
    id_sol = len(SOLICITACOES)+1
    sol = Solicitacao(id_sol, data['cliente_id'], data['servico'], data.get('fotos',[]))
    SOLICITACOES.append(sol)
    return jsonify({'id':sol.id,'status':sol.status}),201

@clientes_bp.route('/pagamentos', methods=['POST'])
def novo_pagamento():
    """Registra pagamento via app"""
    data = request.get_json()
    id_pag = len(PAGAMENTOS_APP)+1
    pag = PagamentoApp(id_pag, data['cliente_id'], data['valor'])
    PAGAMENTOS_APP.append(pag)
    return jsonify({'id':pag.id,'valor':pag.valor,'status':pag.status}),201

@clientes_bp.route('/historico/<int:cliente_id>', methods=['GET'])
def historico_cliente(cliente_id):
    """Retorna histórico de solicitações e pagamentos"""
    historico = [s.__dict__ for s in SOLICITACOES if s.cliente_id==cliente_id]
    pagamentos = [p.__dict__ for p in PAGAMENTOS_APP if p.cliente_id==cliente_id]
    return jsonify({'solicitacoes':historico,'pagamentos':pagamentos})
@clientes_bp.route('/solicitacoes/<int:id_sol>', methods=['PUT'])
def atualizar_solicitacao(id_sol):
    """Atualiza status da solicitação"""
    sol = next((s for s in SOLICITACOES if s.id==id_sol), None)
    if not sol:
        return jsonify({'error':'Solicitação não encontrada'}),404
    data = request.get_json()
    novo_status = data.get('status', sol.status)
    if novo_status != sol.status:
        sol.historico.append({'status': sol.status, 'data': datetime.now().isoformat()})
        sol.status = novo_status
    return jsonify({'id':sol.id,'status':sol.status,'historico':sol.historico})