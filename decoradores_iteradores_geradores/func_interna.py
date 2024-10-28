"""Funções internas inner functions"""

def principal():
    print('executando principal() !')
    
    def interna():
        print('Executando func interna()')
        
    def func2():
        print('executando a func2()')
    
    interna()
    func2()
    
principal()