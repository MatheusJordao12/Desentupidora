from datetime import datetime

class Tecnico:
    """Representa um técnico da desentupidora"""
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.escala = []

class Escala:
    """Representa o agendamento de um técnico"""
    def __init__(self, tecnico_id, data, os_id=None):
        self.tecnico_id = tecnico_id
        self.data = data
        self.os_id = os_id
        self.check_in = None
        self.check_out = None
