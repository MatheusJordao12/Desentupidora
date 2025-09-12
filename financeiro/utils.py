def listar_pagamentos():
    from .routes import PAGAMENTOS
    return [{'id':p.id,'tipo':p.tipo,'valor':p.valor,'descricao':p.descricao} for p in PAGAMENTOS]
# Funções auxiliares
def listar_comissoes():
    from .routes import COMISSOES
    return [{'id':c.id,'tecnico_id':c.tecnico_id,'valor':c.valor} for c in COMISSOES]
