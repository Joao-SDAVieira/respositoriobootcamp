arquivo = open('C:/Users/40417045/OneDrive - Telefonica/Documents/Git_Dio/desafio_git/respositoriobootcamp/manipulacao_arquivos/teste.txt', 'w')

#write escreve a string que voce passar como um só
arquivo.write('Escrevendo dados em um novo arquivo.')

#writelines() recebe uma string ou uma lista, escrevendo da exata mandeira que você passar
arquivo.writelines(['escrevendo', 'um', 'novo', 'texto'])

#adicionando a mesma frase , desta vez com '\n' para pular uma linha

arquivo.writelines(['\n','escrevendo','\n', 'um','\n', 'novo','\n', 'texto'])

arquivo.close()

