from abc import ABC, abstractmethod, abstractproperty 

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        print(f'ligar {__class__.__name__}')
    
    @abstractmethod
    def desligar(self):
        print(f'desligar {__class__.__name__}')
        
    
    '''Para utilizar property em um metodo abstrato é usando abstractproperty + property'''
    
    # @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    '''quando um método de uma classe é um metodo abstrato é necessario passar o 
    método novamente na classe herdeira. OBS: passar o metodo abstrato para a classe filha n é opcional
    é necessario passar.'''
    
    def ligar(self):
        print(f'ligar {__class__.__name__}')
    
    
    def desligar(self):
        print(f'desligar {__class__.__name__}')
        
    '''Passado o property tambem para a classe mae'''
    @property
    def marca(self):
        return f'{__class__.__name__} philco'
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print(f'Ligando {__class__.__name__}')
        
    def desligar(self):
        return f'desligar {__class__.__name__}'

    @property
    def marca(self):
        return f'{__class__.__name__} LG'
        
    
controle = ControleTV()
controle.ligar()
controle.desligar()


print(controle.marca)


controle = ControleArCondicionado()
print(controle.marca)