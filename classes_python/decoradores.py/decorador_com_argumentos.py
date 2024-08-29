""" EXEMPLO SEM ARGS E KWARGS """

# def meu_decorador(funcao):
#     def envelope(nome, b):
#         print("faz algo antes de executar")
#         funcao(nome, b)
#         print("faz algo depois de executar")

#     return envelope

# @meu_decorador
# def ola_mundo(nome, outro_argumento):
#     print(f"olá mundo! {nome}")

# ola_mundo("João", 1000)

""" EXEMPLO COM ARGS E KWARGS"""

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"olá mundo! {nome}, {outro_argumento}")

ola_mundo("João",1000)
