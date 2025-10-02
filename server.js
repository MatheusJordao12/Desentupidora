// server.js
const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const PORT = 3000;

// Middlewares
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

const USERS = [
    { username: 'admin', password: '123456' },
];

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = USERS.find(u => u.username === username && u.password === password);
    if (user){
        res.json({ sucess: true, message: 'Login realizado com sucesso'});
    } else {
        res.status(401).json({ sucess: false, message: 'Usuário ou senha inválidos'});
    }
  );
});

// Teste de rota
app.get("/", (req, res) => {
  res.send("Servidor rodando com Express + SQLite3 🚀");
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
