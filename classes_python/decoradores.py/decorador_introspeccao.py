import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"olá mundo! {nome}, {outro_argumento}")
    return nome.upper()

resultado = ola_mundo("João",1000)
print(resultado)

""" se eu tento chamar a funcao usando o metodo __name__ depois de usar um decorador
a funcao acaba recebendo o nome da outra funcao que chama ela, então é utilizado @functools.wraps"""
print(ola_mundo.__name__)