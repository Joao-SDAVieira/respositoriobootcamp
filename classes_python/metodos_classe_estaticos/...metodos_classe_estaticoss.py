
'''Forma com metodo de instancia'''
"""
class Pessoa:
    def __init__(self, nome = None, idade=None):
        self.nome = nome
        self.idade = idade 
    #cmetodo instancia
    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2022 - ano
        return Pessoa(nome,idade)

p = Pessoa('Guilherme', 28)

print(p.nome, p.idade)

p2 = Pessoa().criar_de_data_nascimento(1994, 3, 21, 'Guilherme')
print(p2.nome, p2.idade)
"""

'''Forma com método de classe'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
    '''!!! utilizado para conseguir passar os argumentos apenas do método para a classe no momento da criacao
    do objeto, sem precisar usar o None, pois nao precisa referenciar a classe explicitamente com self!!!'''
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    '''!!!Utilizado para não precisar referenciar a classe, apenas utilizar o método de dentro dela, sem criar um objeto
    ou passar os atributos da classe!!!'''
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
p = Pessoa('Guilherme', 28)

print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1994, 3, 21, 'Guilherme')
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))