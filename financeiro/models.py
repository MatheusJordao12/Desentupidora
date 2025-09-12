class Pagamento:
    """Representa um pagamento ou comissão"""
    def __init__(self, id, tipo, valor, descricao):
        self.id = id
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.valor = valor
        self.descricao = descricao

class Comissao:
    """Comissão de técnico sobre serviço"""
    def __init__(self, id, tecnico_id, valor):
        self.id = id
        self.tecnico_id = tecnico_id
        self.valor = valor
