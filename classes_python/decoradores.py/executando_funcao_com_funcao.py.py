def mensagem(nome):
    print("executando mensagem")
    return f'Oi {nome}'

# def mensagem_longa(nome):
#     print('Executando mensagem longa')
#     return f'Olá, tudo bem com você {nome}?'

def executar(funcao,nome):
    print("executando a função executar")
    return funcao(nome)
''' 
Nesse ponto, a função chamada é a executar, porém o retorno dela é chamar a função "mensagem" já passando o parametro
dessa função, no caso "nome"
'''
print(executar(mensagem,'Joao'))