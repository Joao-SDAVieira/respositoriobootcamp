class Conta:
    def __init__(self,nro_agencia, saldo=0):
        '''definindo saldo como uma variavel privada (não pode ser acessada, principalmente para alterar seu valor)
        principalmente fora da classe, enquanto nro_agencia é publico'''
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self,valor):
        self._saldo  += valor
    
    def sacar(self,valor):
        self._saldo -= valor
       
    '''criando um metodo apenas para acessar o saldo, apenas como forma de exibição''' 
    def mostrar_saldo(self):
        return self._saldo
    

minha_conta = Conta('1234',100)
minha_conta.depositar(100)
minha_conta.sacar(200)

'''forma errada'''
print(minha_conta._saldo)
print(minha_conta.nro_agencia)

'''forma correta, chamando o método de auxilio'''
print(minha_conta.mostrar_saldo())