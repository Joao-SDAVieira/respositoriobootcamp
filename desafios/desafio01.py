menu = """
[D] Depositar
[S] Sacar
[E] Extrato 
[Q] Sair

"""

saldo = 0
limite_saque = 500
extrato = ''
total_saque = 0
MAX_SAQUE = 3


while True:
    opcao = input(menu + 'Opção: ')
    if opcao.upper() == 'D':
        deposito = int(input('Valor do Depósito:\n= '))
        if deposito > 0:
            saldo += deposito
            print('Deposito executado com sucesso')
            extrato += '\nDeposito: +' + str(deposito)
        else:
            print('!Você precisa inserir um valor positivo válido para depósito!')
    elif opcao.upper() == 'S':
        saque = int(input('Valor do Saque:\n= '))
        if saque <= 0 :
            print('!Você precisa inserir um valor positivo para saque!')
        elif saque > 500:
            print('!O valor do saque é no máximo R$500!')
        elif saque > saldo:
            print('!Saldo insuficiente!')
        elif total_saque >= 3:
            print('!Limite de saque já atingido!')
        else:
            saldo -= saque
            total_saque += 1
            extrato += '\nSaque: -' + str(saque)
            print('Saque relizado com sucesso')

    elif opcao.upper() == 'E':
        print(F'Extrato:\n{extrato}\n\nSaldo: R$ {saldo}')
    elif opcao.upper() == 'Q':
        print('Obrigado por usar nosso sistema.')
        break
    else:
        print("""
Lembre de digitar um valor válido
                """)
        



