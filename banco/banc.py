import sqlite3
import hashlib

conexao = sqlite3.connect(r"C:\Users\GUILHERMEFERREIRAALV\tcc\banco\banco.db")
def criar_banco():
    conexao = sqlite3.connect("sistema_login.db")
    cursor = conexao.cursor()
    
    # Estrutura com cargo e campos de usuário
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL,
        cargo TEXT DEFAULT 'usuario'
    )
    """)
    conexao.commit()
    conexao.close()