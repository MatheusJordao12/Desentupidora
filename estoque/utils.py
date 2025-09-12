def listar_materiais():
    from .routes import MATERIAIS
    return [{'id':m.id,'nome':m.nome,'quantidade':m.quantidade} for m in MATERIAIS]
# Funções auxiliares