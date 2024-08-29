def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        """ 
        chamando a funcao ola_mundo e armazenando o retorno dela na variável resultado
        """
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
