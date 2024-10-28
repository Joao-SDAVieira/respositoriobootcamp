import csv
from pathlib import Path
ROOT_PATH = Path(__file__).parent
def escrevendo_criando_csv():
    try:
        with open(ROOT_PATH / 'usuarios.csv', 'w',newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['id', 'Nome'])
            escritor.writerow(['1','Maria'])
            escritor.writerow(['2','João'])

    except IOError as exc:
        print('erro ao criar o arquivo', exc)
        
# escrevendo_criando_csv()

def lendo_csv_com_reader():
    try:
        with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            # for row in leitor:
            #     '''uma forma de iterar o arquivo'''
            #     print(row[0], row[1])
            COLUNA_ID = 0
            COLUNA_NOME = 1
            # for row in leitor:
            #     '''uma forma de iterar o arquivo'''
            #     print(row[COLUNA_ID], row[COLUNA_NOME])
                
            for idx, row in enumerate(leitor):
                if idx == 0:
                    continue
                print(f'ID: {row[COLUNA_ID]}')
                print(f'Nome: {row[COLUNA_NOME]}')

    except IOError as exc:
        print('erro ao criar o arquivo', exc)
        
lendo_csv_com_reader()


'''FOrma mais usual, uma forma de iterar o conteudo do csv sem traver o cabeçalho, passando ele como chave de um dicionario'''
def lendo_csv_com_dictreader():
    try:
        with open(ROOT_PATH / 'usuarios.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for row in leitor:
                print(row['id'], row['Nome'])
                print(row)

    except IOError as exc:
        print('erro ao criar o arquivo', exc)
lendo_csv_com_dictreader()

