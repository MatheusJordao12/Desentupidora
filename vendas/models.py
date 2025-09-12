class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.historico = []

class Orçamento:
    def __init__(self, id, cliente_id, servico, valor):
        self.id = id
        self.cliente_id = cliente_id
        self.servico = servico
        self.valor = valor
        self.status = "Pendente"
