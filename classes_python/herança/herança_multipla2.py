class Animal:
    def __init__(self, nro_patas):
        print('inicializando a classe')
        self.nro_patas = nro_patas
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)
    def __str__(self):
        return f'{self.__class__.__name__} metodo str'

class Ave(Animal):
    def __init__(self,cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)
    
    """o metodo str só é chamado em uma das classes, no caso a mais próxima da classe que foi chamada"""
    def __str__(self):
        '''chamado depois da classe que herda essa classe'''
        return 'ave metodo str'


class Cachorro(Mamifero):
    pass



class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero,Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        #verificando a ordem em que serão buscadas as heranças, no caso (<class '__main__.Ornitorrinco'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>)
        print(Ornitorrinco.__mro__)
        super().__init__(cor_bico= cor_bico, cor_pelo = cor_pelo, nro_patas = nro_patas)

    def __str__(self):
        '''chamado primeiro'''
        return 'Ornitorricon método str'
class Leao(Mamifero):
    pass


'''Instanciando a classe de herança simples Gato sem kwargs. OBS: Da erro'''
# gato = Gato(4, 'preto')
# print(gato.cor_pelo)

"""Instanciando a classe de herança dupla Ornitorrinco, sem Kwargs. Obs: da erro"""

# ornitorrinco1 = Ornitorrinco(2, "vermelha")
# print(ornitorrinco1)


'''Instanciando ambos com kw, porem, os parametros da classe pai (Animal) pode ser posicional'''
gato2 = Gato('Preto', nro_patas=4)
print(gato2)

ornitorrinco2 = Ornitorrinco(cor_pelo='Azul', nro_patas=2, cor_bico='amarelo')
print(ornitorrinco2)
