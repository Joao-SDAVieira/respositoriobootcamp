from pathlib import Path

'''Com o path do pathlib e possivel acessar o diretorio acima do arquivo que o código está rodando, sem
precisar especificar o caminho no momento de trabalhar com um tipo de arquivo txt, csv etc'''

def not_found_erro():
    try:
        arquivo = open('meu_arquivo.py')
    except FileNotFoundError as exc:
        print('Arquivo n encontrado!')
        print(exc)

# not_found_erro()

def permission_erro():
    ROOT_PATH = Path(__file__).parent

    try:
        arquivo = open(ROOT_PATH / 'novo-diretorio')
    except PermissionError as exc:
        print(f'Não foi possivel abrir o arquivo\nErro: {exc}')
        
# permission_erro()

lista = ['1','2','3','4','5','6']

for i, value in enumerate(lista):
    try:
        print(lista[i-1])
    except IndexError:
        print('primeiro indice')