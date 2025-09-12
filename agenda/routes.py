from flask import Blueprint, jsonify, request
from .models import Tecnico, Escala
from datetime import datetime

agenda_bp = Blueprint('agenda', __name__)

TECNICOS = []
ESCALAS = []

@agenda_bp.route('/tecnicos', methods=['POST'])
def criar_tecnico():
    """Cria um técnico"""
    data = request.get_json()
    tecnico_id = len(TECNICOS) + 1
    tecnico = Tecnico(tecnico_id, data['nome'])
    TECNICOS.append(tecnico)
    return jsonify({'id': tecnico.id, 'nome': tecnico.nome}), 201

@agenda_bp.route('/escala', methods=['POST'])
def criar_escala():
    """Agendar um técnico"""
    data = request.get_json()
    escala = Escala(data['tecnico_id'], data['data'], data.get('os_id'))
    ESCALAS.append(escala)
    return jsonify({'tecnico_id': escala.tecnico_id, 'data': escala.data, 'os_id': escala.os_id}), 201

@agenda_bp.route('/checkin/<int:tecnico_id>', methods=['PUT'])
def checkin(tecnico_id):
    """Registrar check-in do técnico"""
    escala = next((e for e in ESCALAS if e.tecnico_id == tecnico_id), None)
    if not escala:
        return jsonify({'error':'Escala não encontrada'}),404
    escala.check_in = datetime.now().isoformat()
    return jsonify({'tecnico_id': tecnico_id, 'check_in': escala.check_in})

@agenda_bp.route('/checkout/<int:tecnico_id>', methods=['PUT'])
def checkout(tecnico_id):
    """Registrar check-out do técnico"""
    escala = next((e for e in ESCALAS if e.tecnico_id == tecnico_id), None)
    if not escala:
        return jsonify({'error':'Escala não encontrada'}),404
    escala.check_out = datetime.now().isoformat()
    return jsonify({'tecnico_id': tecnico_id, 'check_out': escala.check_out})
