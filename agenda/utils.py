# Funções auxiliares
def listar_escala():
    from .routes import ESCALAS
    return [{'tecnico_id': e.tecnico_id, 'data': e.data, 'os_id': e.os_id} for e in ESCALAS]
