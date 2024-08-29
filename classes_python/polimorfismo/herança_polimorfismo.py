class Passaro:
    def voar(self):
        print("Voando")
    def botar_ovo(self):
        print("Botando ovo")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


""" 
Polimorfismo está justamente em um objeto possuir todos os metodos da classe (no caso "voar") e em outro não, ele
ter uma função diferente, no caso o onjeto que não tem as exatas caracteristicas apenas herda o metodo, mas a ação
é outra
"""
def chamando_passaros(obj):
    obj.voar()
    obj.botar_ovo()

p1 = Pardal()
p2 = Avestruz()

p2.botar_ovo()
chamando_passaros(p1)
chamando_passaros(p2)
