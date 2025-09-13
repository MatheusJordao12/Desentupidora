from flask import Flask, render_template, request, redirect, url_for
import json, os, datetime

app = Flask(__name__)
DATA_FILE = "data.json"

# Função para carregar dados
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Função para salvar dados
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route("/")
def index():
    ordens = load_data()
    pendentes = [os for os in ordens if os["status"] == "pendente"]
    finalizadas = [os for os in ordens if os["status"] == "finalizado"]
    return render_template("index.html", pendentes=pendentes, finalizadas=finalizadas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    cliente = request.form["cliente"]
    servico = request.form["servico"]

    ordens = load_data()
    nova_os = {
        "id": int(datetime.datetime.now().timestamp() * 1000),
        "cliente": cliente,
        "servico": servico,
        "status": "pendente",
        "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    ordens.append(nova_os)
    save_data(ordens)

    return redirect(url_for("index"))

@app.route("/finalizar/<int:os_id>")
def finalizar(os_id):
    ordens = load_data()
    for os_item in ordens:
        if os_item["id"] == os_id:
            os_item["status"] = "finalizado"
    save_data(ordens)
    return redirect(url_for("index"))

@app.route("/excluir/<int:os_id>")
def excluir(os_id):
    ordens = load_data()
    ordens = [os for os in ordens if os["id"] != os_id]
    save_data(ordens)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
