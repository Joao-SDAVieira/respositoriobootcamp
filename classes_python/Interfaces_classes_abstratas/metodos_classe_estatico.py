class Pessoa:
    ''' 
    já dessa forma, utilizando o metodo de classe não é necessário utilizar o None como valor default
    '''
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
    """ Utilizando o metodo de classe "@classmethod", utilizado para caso precise do contexto do 
    método da casse (as variáveis do método construtor da classe)"""
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        """é necessario trocar o ^^ self por "cls", a partr daí o "cls" referencia a classe em si"""
        idade = 2024 - ano
        return cls(nome, idade)
        return Pessoa(nome, idade)
        """subs ^^^^ a classe "Pessoa()" por "cls" """
    
    """ 
    Agora utilizando método estático, @staticmethod, utilizado quando não precisa do methodo
    da classe. Pois sem ele, eu teria que passar todos os parametros para o
    construtor da classe Pessoa ou deixar como none, além de ter que chamar a classe com parênteses e
    utilizar o self no metodo e_maior_idade
    """
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("João", 'Vinte')

# print(p.nome, p.idade)
p2 = Pessoa.criar_de_data_nascimento(2004,3,21, "João")
""" 
jão não é utilizado 
p2 = Pessoa().criar_de_data_nascimento(2004,3,21, "João")
"""
print(p2.nome, p2.idade)

""" 
chamando o método estático
"""
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(2))
