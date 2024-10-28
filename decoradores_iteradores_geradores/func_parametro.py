"""Passagem de função como parametro para outra funcao, com duas formas de passar o parametro da funcao parametro"""

def mensagem(nome):
    print('executando mensagem()')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem_longa()')
    return f'Ola tudo bem com voce {nome}'

#forma 1
def executar_chumbado(funcao):
    print('executando funcao')
    return funcao('joao')

#forma 2
def executar_parametro(funcao,nome):
    print('executando funcao')
    return funcao(nome)

#chamando forma 1
executar_chumbado(mensagem)

#chamando forma 2
executar_parametro(mensagem_longa, 'joao')