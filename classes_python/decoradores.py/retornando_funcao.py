from struct import calcsize


def calculadora(operacao):
    def soma(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def multi(a,b):
        return a*b
    
    def div(a,b):
        return a/b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case '*':
            return multi
        case '/':
            return div

""" 
algumas formas de chamar a mesma função
"""
print(calculadora("+")(a=6,b=3))

op = calculadora('-')
print(op(4,2))
