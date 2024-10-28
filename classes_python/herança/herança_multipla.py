class Animal:
    def __init__(self,nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        """O metodo "super" serve para puxar os atrinutos da classe principal, 
        para reutilizar suas heranças junto a outros atributos da classe filha"""
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self,cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

""" 
Mixin é um tipo de classe muito utilizado em Django acoplar uma função facilmente
a uma classe
"""
class FalarMixin():
    def falar(self):
        return __class__.__name__,'Falando...Falando...'


class Ornitorrinco(Mamifero,Ave,FalarMixin):
    def __init__(self, cor_bico,cor_pelo, nro_patas):
        """
        o método "mro" é utilizado para saber a ordem que classe será interpretada
        """
        print(Ornitorrinco.__mro__)
        """ ou """
        print(Ornitorrinco.mro())
        
        super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico,nro_patas=nro_patas)
    def __str__(self):
        return f"nome da classe {__class__.__name__}"
    




class Gato(Mamifero):
    pass




gato = Gato(nro_patas ="4", cor_pelo="Preto")

print(gato)
ornitorrinco = Ornitorrinco(nro_patas = "2",cor_bico = "Preto/Vermelho", cor_pelo="Vermelho")
print(ornitorrinco)
""" 
chamando a função falar do Mixin que a classe Ornitorrinco está herdando
"""
print(ornitorrinco.falar())
