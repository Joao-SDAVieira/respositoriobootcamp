from ast import Del


class Cachorro:
    '''O método inicializador sempre será chamado antes de qualquer outro método, no caso, o print de init executará
    antes do método falar'''
    def __init__(self, nome, cor, acordado=True):
        print('inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    '''O del sempre removerá a instancia da classe no final do script'''
    def __del__(self):
        print("Removendo a instancia da classe")
        
    def falar(self):
        print('auau')

def criar_cachorro():
    c =  Cachorro('Zeus', "branco/preto", False)
    print(c.nome)

c = Cachorro('cachorro', 'preto')
c.falar()


criar_cachorro()
        