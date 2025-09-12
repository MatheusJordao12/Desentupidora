def gerar_resumo_os():
    from atendimento.routes import ORDENS
    return [{'id':o['id'],'status':o['status']} for o in ORDENS]
# Funções auxiliares