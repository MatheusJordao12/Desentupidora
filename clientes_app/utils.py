def listar_solicitacoes():
    from .routes import SOLICITACOES
    return [{'id':s.id,'cliente_id':s.cliente_id,'servico':s.servico,'status':s.status} for s in SOLICITACOES]
# Funções auxiliares
def listar_clientes():
    from .routes import CLIENTES
    return [{'id':c.id,'nome':c.nome,'telefone':c.telefone,'endereco':c.endereco} for c in CLIENTES]
