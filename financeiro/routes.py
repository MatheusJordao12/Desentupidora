from flask import Blueprint, jsonify, request
from .models import Pagamento, Comissao

financeiro_bp = Blueprint('financeiro', __name__)

PAGAMENTOS = []
COMISSOES = []

@financeiro_bp.route('/pagamentos', methods=['POST'])
def criar_pagamento():
    """Registra um pagamento"""
    data = request.get_json()
    id_pag = len(PAGAMENTOS)+1
    pag = Pagamento(id_pag, data['tipo'], data['valor'], data['descricao'])
    PAGAMENTOS.append(pag)
    return jsonify({'id':pag.id,'tipo':pag.tipo,'valor':pag.valor}),201

@financeiro_bp.route('/comissoes', methods=['POST'])
def criar_comissao():
    """Registra comissão de técnico"""
    data = request.get_json()
    id_com = len(COMISSOES)+1
    com = Comissao(id_com, data['tecnico_id'], data['valor'])
    COMISSOES.append(com)
    return jsonify({'id':com.id,'tecnico_id':com.tecnico_id,'valor':com.valor}),201

@financeiro_bp.route('/resumo', methods=['GET'])
def resumo_financeiro():
    """Resumo financeiro básico"""
    total_entrada = sum(p.valor for p in PAGAMENTOS if p.tipo=='entrada')
    total_saida = sum(p.valor for p in PAGAMENTOS if p.tipo=='saida')
    return jsonify({'total_entrada': total_entrada, 'total_saida': total_saida})
