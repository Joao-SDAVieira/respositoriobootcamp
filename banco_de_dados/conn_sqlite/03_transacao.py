import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

"""A seguir existem duas formas de garantir que todas as querys sejam executadas com sucesso ou nenhuma seja
pois se uma for executada e a outra não, o código pode gerar conflito"""



"""utilizando o with 
o with garante que tudo que seja executado funcione para o commit ser finamente executado"""
with sqlite3.connect(ROOT_PATH / "clientes.sqlite") as conexao:
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?)", ('Teste 2', 'teste2@gmail.com'))
    cursor.execute("INSERT INTO clientes (id,nome,email) VALUES (?,?,?)", (2,'Teste 3', 'teste3@gmail.com'))
    conexao.commit()

"""utilizando o try e comitando só no final"""
try:
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?)", ('Teste 2', 'teste2@gmail.com'))
    cursor.execute("INSERT INTO clientes (id,nome,email) VALUES (?,?,?)", (2,'Teste 3', 'teste3@gmail.com'))
    conexao.commit()
except Exception as a:
    print('Ocorreu um erro', a)
    conexao.rollback()
# finally:
#     conexao.commit()