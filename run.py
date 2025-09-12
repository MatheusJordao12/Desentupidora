from flask import Flask
from config.config import Config

# Importando módulos
from atendimento.routes import atendimento_bp
from agenda.routes import agenda_bp
from vendas.routes import vendas_bp
from financeiro.routes import financeiro_bp
from estoque.routes import estoque_bp
from relatorios.reports import relatorios_bp
from clientes_app.routes import clientes_bp

app = Flask(__name__)
app.config.from_object(Config)

# Registrando blueprints
app.register_blueprint(atendimento_bp, url_prefix='/atendimento')
app.register_blueprint(agenda_bp, url_prefix='/agenda')
app.register_blueprint(vendas_bp, url_prefix='/vendas')
app.register_blueprint(financeiro_bp, url_prefix='/financeiro')
app.register_blueprint(estoque_bp, url_prefix='/estoque')
app.register_blueprint(relatorios_bp, url_prefix='/relatorios')
app.register_blueprint(clientes_bp, url_prefix='/clientes')

@app.route('/')
def home():
    return "Sistema de Desentupidora Online - API funcionando!"

if __name__ == '__main__':
    app.run(debug=True)
