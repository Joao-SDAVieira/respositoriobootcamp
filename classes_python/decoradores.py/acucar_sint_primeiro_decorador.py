# #utilizando açucar sintático no primeiro decorador
# def meu_decorador(funcao):
#     def envelope():
#         print("faz algo antes de executar")
#         funcao()
#         print("faz algo depois de executar")

#     return envelope

# @meu_decorador
# def ola_mundo():
#     print("olá mundo!")

# """ Não é mais necessario o código comentado a seguir devido ao açucar sintático"""
# #ola_mundo = meu_decorador(ola_mundo)
# ola_mundo()




"""Decorador com funções que possui argumentos"""

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo():
    print("olá mundo!")

ola_mundo()
