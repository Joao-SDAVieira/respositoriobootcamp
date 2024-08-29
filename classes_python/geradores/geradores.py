""" Gerador """

def meu_gerador(numeros:list[int]):
    for numero in numeros:
        yield numeros * 2
    

for i in meu_gerador(numeros= [1,2,3,4,5,6,7,7,7]):
    print(i)