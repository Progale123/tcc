import sqlite3
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_banco():
    conexao = sqlite3.connect("sistema_criarconta.db")
    cursor = conexao.cursor()

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

def cadastrar_usuario(nome, email, senha, cargo="usuario"):
    conexao = sqlite3.connect("sistema_login.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO usuarios (nome, email, senha_hash, cargo)
            VALUES (?, ?, ?, ?)
        """, (nome, email, hash_senha(senha), cargo))
        conexao.commit()  
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: email já cadastrado.")
    finally:
        conexao.close()

criar_banco()
cadastrar_usuario("guilherme", "teste123@gmail.com", "senha", "admin")
cadastrar_usuario("João", "joao@email.com", "123456", "estagiario")
cadastrar_usuario("Maria", "maria@email.com", "abc123", "admin")


def informa_dados():
     conexao = sqlite3.connect("sistema_login.db")
     cursor = conexao.cursor()

     nome = input("digite seu nome:")
     if nome !="" :
      print("Campo preenchido, avançando...")
     else:
      print("Campo vazio")

     email = input("Digite seu email:")  
     if email !="" :
      print("Campo preenchido, avançando")
     else:
      print("Campo vazio")

     senha = input("Crie uma senha")
     if senha !="" :
      print("Campo preenchido, avançando")
     else:
      print("Campo vazio") 
     
      conexao.close()