"""Utilizando decorador de duas formas"""

"""forma 1, mais verbosa e pouco usada"""

def forma1():
    def meu_decorador(funcao):
        def envelope():
            print('faaz algo antes de executar')
            funcao()
            print('faaz algo depois de executar')
            
        return envelope

    def ola_mundo():
        print('ola mundo')
        
        
    ola_mundo = meu_decorador(ola_mundo)
    ola_mundo()

forma1()
print('\n\n\n\n')
"""forma 2, menos verbosa usando açucar sintatico, menos verboso"""

def forma2():
        
    def meu_decorador(funcao):
        def envelope():
            print('faaz algo antes de executar')
            funcao()
            print('faaz algo depois de executar')
            
        return envelope

    """esse '@meu_decorador simboliza a atribuição da função ola mundo a 'meu_decorador(ola_mundo)' """
    @meu_decorador
    def ola_mundo():
        print('ola mundo')
        
    '''O acucar substiui a linha comentada'''
    # ola_mundo = meu_decorador(ola_mundo)
    ola_mundo()
    
forma2()

"""utilizando mais de um parametro com kwargs"""
def continuacao():
        
    def meu_decorador(funcao):
        def envelope(*args,**kwargs):
            print('antes da função()')
            funcao(*args,**kwargs)
            print('depois da funcao()')
        return envelope

    @meu_decorador
    def ola_mundo(nome):
        print(f'ola mundo {nome}')
        
    ola_mundo('joao')

continuacao()

