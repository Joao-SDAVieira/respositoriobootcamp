class Pessoa:
    def __init__(self,nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    """ 
    pelo que entendi o properti vai servir para poder utilizar um parametro/atributo sem utilizar o metodo construtor
    """
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    """ 
    OUTRA FORMA DE FAZER SEM O "property"
    """

    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2022 - self._ano_nascimento

pessoa = Pessoa("João", 2004)


print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

""" 
Outra forma de fazer sem o property
"""

print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")