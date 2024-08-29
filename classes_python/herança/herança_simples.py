class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa 
        self.numero_rodas = numero_rodas
    def ligar_motor(self):
        print("Ligando motor\n")
        """uma forma de exibir a cor de um objeto especifico"""
    # def __str__(self):
    #     return self.cor
        """uma forma de exibir os valores de um objeto
        self.__class__ nos tras o nome da class, ex:<class '__main__.Caminhao'>
        porém, queremos o o nome da classe, então utilizando ".__name__",
        ex: Caminhao. Com isso, queremos iterar sobre cada atributo da classe,
        então é utilizado "self.__dict__" para exibir o atributo e seu valor
        ex: {'cor': 'Vermelho', 'placa': 'HGD-09', 'numero_rodas': '10', 'carregado': True}
        uma vez que temos ele em dicionário, queremos que cada chave e valor vire uma 
        tupla em uma lista, usando "__dict__.items()", 
        ex: dict_items([('cor', 'Vermelho'), ('placa', 'HGD-09'), ('numero_rodas', '10'), ('carregado', True)])
        então é feito um for para iterar sobre cada chave e valor desse dicionário
        acrescentando o ", " através do join para cada item do dicionário, e um ' = ' para
        cada chave e valor.
         """
           
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}\n"
class Motocicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    """sobrescrevendo os atrinutos da classe "Caminhão" 
       que são erdados de "Veiculo" """
    def __init__(self, cor, placa, numero_rodas,
    carregado= False):
        """Utilizando a palavra reservada "super" para sobrescrever os valores Caminhao"""
        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"" if self.carregado else "Não"} estou carregado")

caminhão = Caminhao("Vermelho", "HGD-09", "10", True)
print(f"Caminhão Cor: {caminhão.cor}\nCaminhão Placa: {caminhão.placa}\nCaminhão rodas: {caminhão.numero_rodas}")
caminhão.ligar_motor()
caminhão.esta_carregado()

moto = Motocicleta("Azul", "XJX-89YH", "2")
carro = Carro("Preto", "XLXS-72H", "4")
print(caminhão)
print(carro)
print(moto)


# print(moto)
# moto.ligar_motor()


# print(f"A cor do carro é {carro.cor}")
# carro.ligar_motor()
