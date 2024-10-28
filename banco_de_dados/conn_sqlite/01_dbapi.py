import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conexao.cursor()

def criar_tabela(cursor):
    cursor.execute("""CREATE TABLE clientes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100),email VARCHAR(150))""")
# criar_tabela(cursor)


def inserir_registros(cursor, conexao):
    data = ("Guilherme", "gui@gmail.com")
    data = ("Giovanna", "gi@gmail.com")
    """Para inserir dados é utilizado o método execute() com no lugar dos dados a serém interidos, ser utilizado uma
    interrogacao ? por motivos de segurança, e como outro parâmetro ser passado uma tupla ou variável com os dados"""
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?)", data)

    """em seguida do que foi executado é importante usar o commit para salvar as informações"""
    conexao.commit()
    
# inserir_registros(cursor,conexao)

def atualizar_registros(conexao,cursor, nome, email, id):
    data = (nome,email,id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?; ",data)
    conexao.commit()
    
# atualizar_registros(conexao,cursor, "Guilherme Carvalho", 'gui@gmail.com', 1)
# atualizar_registros(conexao,cursor, "Giovanna Carvalho", 'gi@gmail.com', 2)

def excluir_registro(conexao,cursor,id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?; ",data)
    conexao.commit()
    
# excluir_registro(conexao,cursor, 1)

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome,email) VALUES (?,?)",dados)
    conexao.commit()

dados = [
    ('Guilherme', 'guilherme@gmail.com'),
    ('Chappie', 'chappie@gmail.com'),
    ('Melaine', 'melaine@gmail.com'),]


# inserir_muitos(conexao,cursor,dados)
def consultando_na_base_de_dados():
    def recuperar_cliente(cursor, id):
        cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
        return cursor.fetchone()


    cliente = recuperar_cliente(cursor, 2)
    print(cliente)

    def listar_clientes(cursor):
        return cursor.execute("SELECT * FROM clientes")
        
    clientes = listar_clientes(cursor)

    print('--------------')

    for cliente in clientes:
        print(cliente)
# consultando_na_base_de_dados()


def consultando_row_factory(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

consulta = consultando_row_factory(cursor,2)

print(dict(consulta))
