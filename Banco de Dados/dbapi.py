import sqlite3 # Importando o SGBD SQLite.
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Conectando nosso Banco.
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor() # O cursor permite que você execute comandos SQL.
cursor.row_factory = sqlite3.Row

# Criando a Tabela Clientes.
def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))") 
    conexao.commit()

# Inserindo dados no registro.
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit() # Salvando os dados para que seja mandado para a pasta "meu_banco.sqlite"

# Atualizando registros.
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

# Excluindo registro.
def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

# Inserindo vários registros.
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()

# Listando um Registro.
def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

# Listando todos os registros.
def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;") # Listando em ordem alfabética decrescente.

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])

print(f'Seja bem vindo(a) {cliente["nome"]}!')

# Inserção de muitos Dados.
# dados = [
#     ("Kaynan Oliveira", "kaynanoliveira@gmail.com"),
#     ("Kevin N.", "kevin@gmail.com"),
#     ("Matheus", "matheus@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)