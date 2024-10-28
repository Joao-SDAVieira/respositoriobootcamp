from pathlib import Path

'''Com o path do pathlib e possivel acessar o diretorio acima do arquivo que o código está rodando, sem
precisar especificar o caminho no momento de trabalhar com um tipo de arquivo txt, csv etc'''
ROOT_PATH = Path(__file__).parent


'''Uma das principais boas praticas ao trabalhar com arquivos no python e utilizar o with
o with faz com que voce possa trabalhar com o arquivo dentro do bloco dele e o arquivo 
sera fechado automaticamente quando o bloco terminar '''
def utilizando_with():
    with open(ROOT_PATH / 'lorem.txt') as arquivo:
        print('Lendo o arquivo', arquivo)

    '''esse print n funcionará pois o arquivo foi fechado'''
    print(arquivo.read())

# utilizando_with()

def utilizando_try():
    
    try:
        '''tentando abrir um arquivo que nao existe utilizando with (dara erro)'''
        with open(ROOT_PATH / '1lorem.txt') as arquivo:
            print('Lendo o arquivo', arquivo)
            
            '''esse print n funcionará pois o arquivo foi fechado'''
            print(arquivo.read())
    except IOError as exc:
        print('Erro ao abrir o arquivo', exc)
        
# utilizando_try()

'''Outra boa-pratica seria colocar o tipo de codigo, ex utf-8 ou ascii'''
def utilizando_encoding_w():
    try:
        with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding = 'utf-8') as arquivo:
            arquivo.write('Aprendendo a manipular arquivos utilizando python')
            arquivo.write('Aprendendo a manipular arquivos utilizando pythonŶŶŶ')
            
    except IOError as exc:
        print('Erro ao abrir o arquivo', exc)
    
utilizando_encoding_w()

def utilizando_encoding_r():
    try:
        with open(ROOT_PATH / 'arquivo-utf-8.txt', 'r', encoding = 'ascii') as arquivo:
            print(arquivo.read())
            
    except IOError as exc:
        print('Erro ao abrir o arquivo', exc)
    except UnicodeDecodeError as exc:
        print('erro de formatação do arquivo: ',exc)
        
utilizando_encoding_r()