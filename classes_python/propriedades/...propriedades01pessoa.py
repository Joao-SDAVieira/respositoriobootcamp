class Pessoa:
    def __init__(self, nome,ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    '''A forma mais usual das propriedades'''
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
    
pessoa1 = Pessoa('Joao', 2004)
print(f'Nome: {pessoa1._nome}\tIdade: {pessoa1.idade}')
