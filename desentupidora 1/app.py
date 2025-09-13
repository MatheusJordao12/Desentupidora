from flask import Flask, render_template, request, redirect, url_for
import json
import os
import uuid
import datetime

app = Flask(__name__)

# Arquivo para salvar os dados
DATA_FILE = "data.json"

# Função para carregar dados do arquivo JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Função para salvar dados no arquivo JSON
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Rota principal
@app.route("/")
def index():
    ordens = load_data()
    return render_template("index.html", ordens=ordens)

# Rota para adicionar OS
@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        cliente = request.form.get("cliente", "").strip()
        servico = request.form.get("servico", "").strip()

        if cliente and servico:
            ordens = load_data()
            nova_os = {
                "id": uuid.uuid4().hex,
                "cliente": cliente,
                "servico": servico,
                "status": "pendente",
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
            ordens.append(nova_os)
            save_data(ordens)

        return redirect(url_for("index"))

    return redirect(url_for("index"))

# Rota para finalizar OS
@app.route("/finalizar/<id>")
def finalizar(id):
    ordens = load_data()
    for os_item in ordens:
        if os_item["id"] == id:
            os_item["status"] = "finalizado"
            break
    save_data(ordens)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
