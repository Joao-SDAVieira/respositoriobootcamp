class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        #atributos
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print('Buzinando')
    def parar(self):
        print('Parando...\nParou')
    def correr(self):
        print('Correndo...')
    def __str__(self):
        # return f'\nBicicleta:\nCor: {self.cor}, Modelo: {self.modelo}\n'
        return f'\n{self.__class__.__name__}:\nCor: {self.cor}, Modelo: {self.modelo}\n'
        # self.cor = 'azul'
        # self.modelo = 'algum modelo'
        # self.ano = '2004'
        # self.valor = '900 reais'

bike_1 = Bicicleta('azul', 'algum modelo', 2004, '900 reais')
bike_1.buzinar()
bike_1.parar()
bike_1.correr()
print(bike_1.cor,bike_1.modelo)
print(bike_1)
