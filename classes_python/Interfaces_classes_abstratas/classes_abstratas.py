from abc import ABC, abstractmethod

'''
O método 'abc' faz com que os métodos da classe abstrata tenham que ser instanciados
dentro da classe que herda a classe abstrata, não instânciando diretamente
'''

"""
Declarando que a classe Controle_Remoto é uma classe abstrata
"""


class ControleRemoto(ABC):
    """
    Fazendo com que os métodos ligar e desligar da classe abstrata são metodos abstrados
    Com isso a classe filha não herdará esses métodos
    """

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    """Tendo que passar os métodos novamente mesmo herdando a classe Controle_Remoto"""
    def desligar(self):
        print("Desligando a TV")

class ControleArCondicionado(ControleRemoto):
    """
    No conceito de classes abstratas, todos os métodos abstratos da classe abstrata
    precisam ser passados
    Nesse caso, o só foi passado o método "ligar" para o ar condicionado, logo, não funcionara
    porque o método "desligar" e, controleremoto também é abstrato
    """
    def ligar(self):
        print("Ligando o ar-condicionado")


controle_remoto = ControleTV()
controle_remoto.ligar()
controle_remoto.desligar()

"""
chamando o método ligar sem o desligar ser passado na classe filha, não funcionará...
"""
# controle_remoto = ControleArCondicionado()
# controle_remoto.ligar()



