arquivo = open('/Users/40417045/OneDrive - Telefonica/Documents/Git_Dio/desafio_git/respositoriobootcamp/manipulacao_arquivos/lorem.txt', 'r')

#utilizando apenas read() é retornada a string completa do arquivo
# print(arquivo.read())
def utilizando_readline():
    
    '''Cada print vai exibir uma linha do arquivo.txt em sequencia, o primeiro readline() a primeira linha, o segundo
    a segundo e assim por diante'''
    # print(arquivo.readline())
    # print(arquivo.readline())
    # print(arquivo.readline())
    # print(arquivo.readline())
    # print(arquivo.readline())
    # print(arquivo.readline())
    '''é possível tbm utilizar o for com readline(), onde irá iterar a linha atual (aparentemente pouco eficaz)'''
    
    for caracter in arquivo.readline():
        print(caracter)

# utilizando_readline()

def utilizando_readlineS():
    """já o readlines() irá retornar uma lista onde cada linha é um indice/valor da lista"""
    print('\n\n\n',arquivo.readlines(),'\n\n\n')
    # for linha in arquivo.readlines():
    #     print(linha)



# utilizando_readlineS()
while len(linha := arquivo.readline()):
    print(len(linha := arquivo.readline()))
arquivo.close()