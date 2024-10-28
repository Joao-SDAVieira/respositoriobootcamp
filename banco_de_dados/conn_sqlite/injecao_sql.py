import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

"""uma boa prática é utilizar tupla para passar a query, utilizando interrogacao ? no lugar da variável
pois se houver algum input do usuário pode ocorrer um input errado por inserção errada ou usuario
mal intencionado, no caso abaixo por exemplo pode-se colocar uma condição True ou o próprio 
true para complementar a query, ou incrementar a query com diversas outras coisas"""
def forma_insegura():
    id_cliente = input('Digite o id do cliente')
    cursor.execute(f'SELECT * FROM clientes WHERE id={id_cliente}')
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(dict(cliente))
forma_insegura()

def forma_segura():
    id_cliente = input('Digite o id do cliente')
    #passando o valor com interrogacao e tupla 
    cursor.execute(f'SELECT * FROM clientes WHERE id=?', (id_cliente,))
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(dict(cliente))