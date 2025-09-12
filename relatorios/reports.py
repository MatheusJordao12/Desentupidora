from flask import Blueprint, jsonify
from datetime import datetime
from atendimento.routes import ORDENS
from agenda.routes import ESCALAS

relatorios_bp = Blueprint('relatorios', __name__)

@relatorios_bp.route('/desempenho', methods=['GET'])
def desempenho_tecnicos():
    """Calcula tempo médio de atendimento"""
    relatorio = []
    for e in ESCALAS:
        if e.check_in and e.check_out:
            inicio = datetime.fromisoformat(e.check_in)
            fim = datetime.fromisoformat(e.check_out)
            duracao = (fim - inicio).total_seconds()/60
            relatorio.append({'tecnico_id': e.tecnico_id, 'duracao_min': duracao})
    return jsonify(relatorio)

@relatorios_bp.route('/mapa_calor', methods=['GET'])
def mapa_calor():
    """Exemplo de mapa de calor de atendimentos por dia"""
    mapa = {}
    for o in ORDENS:
        data = o.get('historico')[0] if o.get('historico') else 'sem_data'
        mapa[data] = mapa.get(data,0)+1
    return jsonify(mapa)
