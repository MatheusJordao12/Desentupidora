// server.js
const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const PORT = 3000;

// Middlewares
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "public"))); // Servir arquivos frontend

// Criar conexão com banco
const db = new sqlite3.Database("./banco.db", (err) => {
  if (err) {
    console.error("❌ Erro ao conectar ao SQLite:", err.message);
    process.exit(1);
  }
  console.log("✅ Conectado ao SQLite.");

  // Criar tabela de usuários
  db.run(
    `CREATE TABLE IF NOT EXISTS usuarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE,
      password TEXT
    )`,
    (err) => {
      if (err) {
        console.error("❌ Erro ao criar tabela:", err.message);
      } else {
        console.log("Tabela 'usuarios' pronta.");

        // Inserir usuário inicial apenas se não existir
        db.get(`SELECT * FROM usuarios WHERE username = ?`, ["admin"], (err, row) => {
          if (err) {
            console.error("Erro ao verificar usuário:", err.message);
          } else if (!row) {
            db.run(`INSERT INTO usuarios (username, password) VALUES (?, ?)`, ["admin", "123456"], (err) => {
              if (err) console.error("Erro ao inserir usuário:", err.message);
              else console.log("Usuário 'admin' criado com sucesso!");
            });
          }
        });
      }
    }
  );
});

// Rota de login
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  db.get(
    `SELECT * FROM usuarios WHERE username = ? AND password = ?`,
    [username, password],
    (err, row) => {
      if (err) return res.status(500).json({ success: false, message: "Erro no servidor" });
      if (row) return res.json({ success: true, message: "Login bem-sucedido" });
      else return res.status(401).json({ success: false, message: "Usuário ou senha inválidos" });
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
