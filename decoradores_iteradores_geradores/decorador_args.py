"""Decorador utilizando mais de um parametro"""
def utilizando_args():
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
    
# utilizando_args()

def sem_utilizar_args():
    def meu_decorador(funcao):
        def envelope(nome,b):
            print('antes da função()')
            funcao(nome,b)
            print('depois da funcao()')
        return envelope

    @meu_decorador
    def ola_mundo(nome, outro_argumento):
        print(f'ola mundo {nome} {outro_argumento}')
        
    ola_mundo('joao', 2)
    
# sem_utilizar_args()

def decorador_retorno():
    def meu_decorador(funcao):
        def envelope(*args,**kwargs):
            print('antes da função()')
            #2 - o retorno é armazenado
            retorno = funcao(*args,**kwargs)
            print('depois da funcao()')
            print(retorno)
        return envelope

    @meu_decorador
    def ola_mundo(nome):
        print(f'ola mundo {nome}')
        #1 - dessa vez o decorador possui um retorno 
        return (nome.upper())
        
    ola_mundo('joao')



"""a razão desse functools é para que quando você chame "funcao.__name__" não aparecça o envelope, que é
o cara que chama a função decorada. Mas para que isso serviria não foi explicado"""
decorador_retorno()
import functools

def decorador_introspeccao():
    def meu_decorador(funcao):
        @functools.wraps(funcao)
        def envelope(*args,**kwargs):
            print('antes da função()')
            funcao(*args,**kwargs)
            print('depois da funcao()')
        return envelope

    @meu_decorador
    def ola_mundo(nome):
        print(f'ola mundo {nome}')
    
    print(ola_mundo.__name__)    
    ola_mundo('joao\n\n')

    
decorador_introspeccao()