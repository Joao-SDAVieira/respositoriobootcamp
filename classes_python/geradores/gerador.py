'''O gerador é uma forma mais otimizada de fazer a iteração no python'''

def meu_gerador(numeros:list[int]):
    for numero in numeros:
        #yield é semelhante ao return
        yield numero*2
        
for i in meu_gerador([1,2,3,4,5]):
    print(i)
    