class Material:
    """Representa um item do estoque"""
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.historico = []
    def adicionar_estoque(self, quantidade, descricao):
        self.quantidade += quantidade
        self.historico.append({'tipo': 'entrada', 'quantidade': quantidade, 'descricao': descricao})

    def remover_estoque(self, quantidade, descricao):
        self.quantidade -= quantidade
        self.historico.append({'tipo': 'saida', 'quantidade': quantidade, 'descricao': descricao})
