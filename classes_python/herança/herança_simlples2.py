class Veículo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
    
    def ligar_motor(self):
        '''Esse class.name trará o nome da classe, isso também vale para as heranças, ou seja, se estiver
        na classe Motocicleta que herda veículo ainda será o class.name Veículo.'''
        print('ligando motor', self.__class__.__name__)
        
class Motocicleta(Veículo):
    pass

class Carro(Veículo):
    pass

class Caminhao(Veículo):
    '''Esse método só existirá em caminhao'''
    
    def __init__(self,cor, placa, nro_rodas,carregado):
        super().__init__(cor,placa,nro_rodas)
        self.carregado = carregado
        '''Como o Caminhao herda Veiculo, se ele tiver o método init próprio pode gerar conflitos, pois o caminhão pode 
        possuir um atributo próprio, então é usado super().init e passado os metodos da classe pai depois
        do metodo construtor da classe filha, corrigindo assim algum erro possivel'''
    def abrir_carga(self):
        print('abrindo carga')

moto1 = Motocicleta('branco', 'placa', '2')
moto1.ligar_motor()


carro1 = Carro('preto', 'placa', '4')
carro1.ligar_motor()

caminhao1 = Caminhao('preto', 'placa', '8',False)
caminhao1.ligar_motor()

