from abc import ABC, abstractmethod
from datetime import datetime

class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self.contas = []
        
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf,nome, data_nascimento):
        self._cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        super().__init__(endereco)
        
    @property
    def cpf(self):
        return self._cpf


class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        saque_maior_zero = valor > 0
        saldo_suficiente = valor > self._saldo
        
        if saldo_suficiente:
            print(f'Seu saldo {self._saldo} é insuficiente para essa transação')
        
        elif saque_maior_zero:
            self._saldo -= valor
            print('Sua transação foi realizada com sucesso!')
            return saque_maior_zero #True
        
        else:
            print('A operação falhou...')
        return False

    
    def depositar(self, valor):
        deposito_maior_zero = valor>0
        if deposito_maior_zero:
            self._saldo += valor
            print('Deposito realizado com sucesso!')
            return True
        else:
            print(f'Impossível realizar o depósito, valor depositado "{valor}" não é válido!')
            
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saque = 3):
        self._limite = limite
        self._limite_saque = limite_saque
        super().__init__(cliente, numero)
        
    def sacar(self, valor):
        nro_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
                         )
        excedeu_limite = valor > self._limite
        excedeu_saques = nro_saques > 3
        if excedeu_limite:
            print(f'Você excedeu o limite do valor do saque. Valor do saque: {valor}\n Limite do saque {self._limite}')
        
        elif excedeu_saques:
            print(f'O limite de saques ({self._limite_saque}) foi atingido.')
        else:
            return super().sacar(valor=valor)
        return False
    
    def __str__(self):
        return f"Agencia: {self.agencia}\n C/C: {self.numero}\n Titular: {self.cliente}"
        
             
class Historico:
    def __init__(self) -> None:
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append({'tipo': transacao.__class__.__name__, 
                                 'valor': transacao.valor, 
                                 'data': datetime.now()})


class Transacao(ABC):
    
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self,conta):
        pass


class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            print('sucesso transacao')


class Deposito(Transacao):
    def __init__(self,valor) -> None:
        self._valor = valor

    @property
    def valor(self):        
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            print('sucesso transacao', conta.historico.adicionar_transacao(self))
    

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(menu)

def filtrar_cliente(cpf,clientes):
    
    fill_clientes = []
    for cliente in clientes:
        if cliente.cpf == cpf:
            fill_clientes.append(cliente)
            print('cliente encontrado', cliente)
    
    return fill_clientes[0] if fill_clientes else None  

def recuperar_conta(cliente):
    if not cliente.contas:
        return
    return cliente.contas[0]


def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print('Cliente não encontrado!')
        return 
    valor = float(input('Informe o valor do deposito: '))
    transacao = Deposito(valor)
    conta = recuperar_conta(cliente)
    
    if not conta:
        return
    cliente.realizar_transacao(conta,transacao)

def sacar(clientes):
    cpf = input('Insira o cpf do cliente: ')
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print('Cliente não encontrado')
        return
    
    valor = float(input('Informe o Valor de Saque: '))
    
    conta = recuperar_conta(cliente)
    
    transacao = Saque(valor)
    
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)
    
def exibir_extrato(clientes):
    cpf = input('Insira seu cpf: ')
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print('Cliente não encontrado!')
        return
        
    conta  = recuperar_conta(cliente)
    
    if not conta:
        return
    
    print('\n================== EXTRATO ==================')
    
    transacoes = conta.historico.transacoes
    
    extrato = ''
    
    if not transacoes:
        extrato = 'Não foram realizadas trasações!'
    
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}\n\t:R$ {transacao['valor']}'
            
    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo}')
    print('\n================== EXTRATO ==================')

def criar_cliente(clientes):
    cpf = input('Insira o cpf (somente números): ')
    cliente = filtrar_cliente(cpf,clientes)
    
    if cliente:
        print('Já existe um cliente com esse cpf:')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (logradouro,nro - bairro - cidade/sigla estado): ')
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf = cpf, endereco=endereco)
    clientes.append(cliente)
    
    print('\n==Cliente criado com sucesso== ')

def criar_conta(num_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print('Não foi possível criar a conta, cliente não encontrado!')
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=num_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print('\nConta criada com sucesso!')

def listar_contas(contas):
    if not contas:
        print('Não há nenhuma conta para listar!')
    for conta in contas:
        print('='*20)
        print(conta)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
            
        elif opcao == "s":
            sacar(clientes)
            
        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()