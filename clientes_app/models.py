class Solicitacao:
    """Solicitação de serviço do cliente"""
    def __init__(self, id, cliente_id, servico, fotos=[]):
        self.id = id
        self.cliente_id = cliente_id
        self.servico = servico
        self.fotos = fotos
        self.status = 'Pendente'

class PagamentoApp:
    """Pagamento feito via app"""
    def __init__(self, id, cliente_id, valor):
        self.id = id
        self.cliente_id = cliente_id
        self.valor = valor
        self.status = 'Pendente'
        self.historico = [] # Histórico de alterações de status