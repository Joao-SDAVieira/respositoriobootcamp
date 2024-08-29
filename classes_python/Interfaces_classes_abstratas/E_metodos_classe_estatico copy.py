
"""
dessa forma que está disposta o código é complexo, para utilizar o metodo criar data de nascimento
os parametros de pessoa precisa, ter um valor padrão "None", além de precisar instanciar
a classe para chamar a função
"""
class Pessoa:
    def __init__(self, nome=None, idade = None):
        self.nome = nome
        self.idade = idade 
    
    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)

p = Pessoa("João", 'Vinte')

# print(p.nome, p.idade)
"""instanciando a classe e chamando a função"""
p2 = Pessoa().criar_de_data_nascimento(2004,3,21, "João")
print(p2.nome, p2.idade)