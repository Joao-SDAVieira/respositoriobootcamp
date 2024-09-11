


class Bicicleta:
    
    """
    metodo "__init__" é o inicializador da classe
    """
    def __init__(self, cor, modelo, ano, valor):
        """ self é uma refeência ao próprio objeto, passa a instancia do obj que foi passado"""
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        # idade = 2024 -self.ano
    
    """ as funções de uma classe é chamada de método, onde é necessár io passar o self para instanciar o obj"""
    def buzinar(self):
        if (2024 - self.ano) < 24:
            print('buzinando')
        else:
            print('Bicicletas mais novas não possuem buzina, geralmente possuem sino')
            
    
    def empinar(self):
        print('elevando o pneu da bicicleta')
        
    """Verificando se a bicicleta consegue empinar"""
    def consegue_empinar(self):
        if self.ano > 2000:
            self.empinar()
        else:
            print('não é possível empinar')
    
    
    def __str__(self):
        """exibindo o nome dos atributos da classe e a classe, self.__dict__ são os atributos e self.__class__.__name__ o nome da classe"""
        # return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}'
        # return f'{self.__class__.__name__}'
        return f'{self.__dict__.items()}'
        
        

objeto_caloi = Bicicleta('vermelha', 'caloi', 2000, 600)

objeto_caloi.buzinar()

"""duas formas de chamar o método do obejto"""
objeto_caloi.consegue_empinar()
Bicicleta.empinar(objeto_caloi)

print(objeto_caloi)