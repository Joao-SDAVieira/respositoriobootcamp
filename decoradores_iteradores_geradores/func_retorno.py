"""retornando uma funcao dentro de uma função"""

def calculadora(operacao):
    def soma(a,b):
        return a+b
    def subtracao(a,b):
        return a-b
    def multi(a,b):
        return a*b
    def div(a,b):
        return a/b
    
    match operacao:
        case '+':
            return soma
        case '-':
            return subtracao
        case '*':
            return multi
        case '/':
            return div
        
#primeira forma, chamando primeiro a primeira função e depois o parametro da funcao retorno
print(calculadora('+')(2,2))

"""segunda forma, armazenando a funcao retorno dentro de uma variavel e chamando a variavel 
como se fosse uma funcao, afinal, ela é uma funcao, pois recebe uma"""

funcao_retorno = calculadora('+')
print(funcao_retorno(2,2))