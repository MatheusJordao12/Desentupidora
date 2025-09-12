def listar_orcamentos():
    from .routes import ORCAMENTOS
    return [{'id':o.id,'cliente_id':o.cliente_id,'servico':o.servico,'valor':o.valor,'status':o.status} for o in ORCAMENTOS]
# Funções auxiliares