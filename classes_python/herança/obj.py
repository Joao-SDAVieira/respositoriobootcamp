class MaquinaLavar:
    def __init__(self,cor, tamanho, qtd_servicos):
        self.cor = cor
        self.tamanho = tamanho
        self.qtd_servicos = qtd_servicos

    def encher(self):
        print(f'{self} enchendo de água')
    
    def lavar(self):
        print(f'{self} lavando')
        
        
class Pia:
    def __init__(self, altura, ejetar_agua):
        self.altura = altura
        self.ejetar_agua = ejetar_agua
    
class LavaLoucas(MaquinaLavar,Pia):
    def __init__(self,secagem, humidecer_sujeira, economizar_energia, **kwargs):
        self.secagem = secagem
        self.humidecer_sujeira = humidecer_sujeira
        self.economizar_energia = economizar_energia
        super(MaquinaLavar).__init__(**kwargs)
        
        
    def printar(self):
        return f'print lavaloucas'
    
    def __str__(self):
        return f'{self.__class__.__name__}:{self.__dict__}'
    
lava_loucas_brastemp = LavaLoucas('20 min','10 min','Verdadeiro', cor = 'algumacor', tamanho = 'algumtamanho', qtd_servicos = 'alguma qtd', altura = 'altura: 90 cm', ejetar_agua = 'ejetartrue')

# lava_loucas_brastemp