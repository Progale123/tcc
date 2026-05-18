const express = require("express");
const sqlite3 = require("sqlite3").verbose();

const app = express();

app.use(express.json());


const db = new sqlite3.Database("./nexadesk.db");


db.run(`
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    senha TEXT,
    cargo TEXT
)
`);

app.post("/cadastro", (req, res) => {

    const { email, senha, cargo } = req.body;

    db.run(
        "INSERT INTO usuarios (email, senha, cargo) VALUES (?, ?, ?)",
        [email, senha, cargo],
        function(err) {

            if (err) {
                return res.status(500).json(err);
            }

            res.json({
                mensagem: "Usuário criado!",
                id: this.lastID
            });

        }
    );

});


app.listen(3000, () => {
    console.log("Servidor rodando!");
});