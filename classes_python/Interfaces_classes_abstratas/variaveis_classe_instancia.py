class Estudante:
    """
    variável de classe, são váriaveis que a partir do momento que você altera para um objeto, 
    altera para todos, um ex é;
    """
    escola = "DIO"

    def __init__(self, nome, nro_matricula):
        '''
        variáveis de instância são as váriáveis passadas do método da classe, caso elas sejam ateradas
        só será alterada para o objeto em questão
        '''
        self.nome = nome 
        self.nro_matricula = nro_matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.nro_matricula} - {self.escola}"

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Geovana", 2)
aluno_3 = Estudante("Rodolfo", 3)
print(aluno_1)
print(aluno_2)
print(aluno_3)
'''
desta forma, se eu alterar a variavel de classe, altera em todos os objetos
'''
Estudante.escola = "DIO.me"
""" 
dessa forma, apenas está mudando apenas o objeto, a variável de instância
"""
aluno_1.escola = "VIVO"
print(aluno_1)
print(aluno_2)
print(aluno_3)