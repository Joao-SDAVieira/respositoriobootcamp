class Estudante:
    escola = 'DIO'
    
    def __init__(self, nome, matricula) -> None:
        self.nome = nome 
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('Giovanna', 2)

#mudando o tributo da classe apenas para um objeto (desta forma, o objeto sempre terá o valor definido)
# aluno_1.escola = 'Python'
print(aluno_1)
print(aluno_2)

#mudando o atributo da classe para a classe (consequentemente para todos os obj)
Estudante.escola = 'Alura'
print(aluno_1)
print(aluno_2)