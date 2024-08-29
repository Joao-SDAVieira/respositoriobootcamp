#inner function
def principal():
    print('Executando a função principal')

    def funcao_interna():
        print("Executando a função interna")

    def funcao_2():
        print("Executando funcao 2")
    
    funcao_interna()
    funcao_2()

principal()