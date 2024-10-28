"""O Iterador serve para iterar uma classe de forma mais eficiente"""
'''Iterador, ao contrário do gerador, é utilizado para fazer uma iteração de algo mais complexo'''
class MeuIterador:
    def __init__(self, iteravel:list[int]):
        self.iteravel = iteravel
        self.contador = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        # try:
        if self.contador <len(self.iteravel):
            numero = self.iteravel[self.contador] 
            self.contador += 1
            return numero *2
        # except IndexError:
        else:
            raise StopIteration
    
for i in MeuIterador([0,1,2,3,4,5,6,7,8,9,10]):
    print(i)