from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        # aqui você pegaria os dados do formulário
        nome = request.form['nome']
        telefone = request.form['telefone']
        # salvar no banco depois...
        return redirect(url_for('index'))
    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(debug=True)
