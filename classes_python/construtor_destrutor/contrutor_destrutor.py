class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe... ")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def __del__(self):
        print("Removendo a instancia da classe")

    def falar(self):
        print("Auau")

def criar_cachorro():
    c = Cachorro ("Zeus", "Preto e Branco", False)
    print(c.nome)

# c = Cachorro("Char", "Amarelo")
# c.falar()
criar_cachorro()