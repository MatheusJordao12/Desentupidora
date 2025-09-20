const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();

const PORT = 3000

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

const USERS = [
    { username: 'admin' , password: '123456' },
    
];



app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = USERS.find(u => u.username === username && u.password === password);
    if (user){
        res.json({ sucess: true, message: 'Login realizado com sucesso'});
    } else {
        res.status(401).json({ sucess: false, message: 'Usuário ou senha inválidos'});
    }
});

app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
})

app.post("financeiro.html", async (req, res) => {
  try {
    const { tipo, descricao, valor } = req.body;
    const result = await pool.query(
      "INSERT INTO registros (tipo, descricao, valor) VALUES ($1, $2, $3) RETURNING *",
      [tipo, descricao, valor]
    );
    res.json(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Erro ao inserir registro" });
  }
});

app.get("financeiro.html", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM registros ORDER BY data DESC");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Erro ao buscar registros" });
  }
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});