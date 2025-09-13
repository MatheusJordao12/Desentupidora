from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

DB_NAME = "database.db"

# -------------------------
# Funções auxiliares
# -------------------------
def get_db():
    conn = sqlite3.connect(DB_NAME)
    return conn, conn.cursor()

def get_user(username, senha):
    conn, cursor = get_db()
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND senha=?", (username, senha))
    user = cursor.fetchone()
    conn.close()
    return user

def get_ordens():
    conn, cursor = get_db()
    cursor.execute("SELECT * FROM ordens")
    ordens = cursor.fetchall()
    conn.close()
    return ordens

def get_financeiro():
    conn, cursor = get_db()
    cursor.execute("SELECT * FROM financeiro")
    registros = cursor.fetchall()
    conn.close()
    return registros

# -------------------------
# Rotas
# -------------------------

# Página inicial → redireciona para login
@app.route("/")
def home():
    return redirect(url_for("login"))

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]
        user = get_user(username, senha)
        if user:
            session["user"] = {"id": user[0], "username": user[1], "tipo": user[3]}
            return redirect(url_for("index"))
        else:
            return "Usuário ou senha inválidos"
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# Lista de ordens
@app.route("/index")
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    ordens = get_ordens()
    user = session["user"]
    return render_template("index.html", ordens=ordens, user=user)

# Adicionar OS
@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        servico = request.form["servico"]

        # Inserir cliente
        cliente_id = str(uuid.uuid4())
        conn, cursor = get_db()
        cursor.execute("INSERT INTO clientes (id, nome, telefone, endereco) VALUES (?, ?, ?, ?)",
                       (cliente_id, nome, telefone, endereco))
        
        # Inserir ordem
        os_id = str(uuid.uuid4())
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cursor.execute("INSERT INTO ordens (id, cliente_id, servico, status, data) VALUES (?, ?, ?, ?, ?)",
                       (os_id, cliente_id, servico, "pendente", data))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("adicionar.html")

# Finalizar OS
@app.route("/finalizar/<id>")
def finalizar(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn, cursor = get_db()
    cursor.execute("UPDATE ordens SET status='finalizado' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

# Financeiro
@app.route("/financeiro", methods=["GET", "POST"])
def financeiro():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        tipo = request.form["tipo"]
        descricao = request.form["descricao"]
        valor = float(request.form["valor"])
        reg_id = str(uuid.uuid4())
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conn, cursor = get_db()
        cursor.execute("INSERT INTO financeiro (id, tipo, descricao, valor, data) VALUES (?, ?, ?, ?, ?)",
                       (reg_id, tipo, descricao, valor, data))
        conn.commit()
        conn.close()
        return redirect(url_for("financeiro"))

    registros = get_financeiro()
    return render_template("financeiro.html", registros=registros)

# -------------------------
# Rodar o app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
