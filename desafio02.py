menu = """
[c] Criar usuário
[cc] Criar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []

conta_corrente = []
numero_conta = 1
agencia = '0001'



def deposito(saldo_func,valor_func,extrato_func,/):

    if valor_func > 0:
        saldo_func += valor_func
        extrato_func += f"Depósito: R$ {valor_func:.2f}\n"
        return saldo_func,extrato_func
    else:
        print("Operação falhou! O valor informado é inválido.")

def saque(*,saldo,valor,limite,LIMITE_SAQUES,extrato,numero_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")

def extrato_def(extrato,/,*,saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# def criar_usuario(*,username, userbirthdate, user_cpf, useruseraddress):
#     username

def criar_usuario(users):
    cpf_usuario = input("CPF:\n")
    usuario_verificado = verificar_usuario(cpf_usuario)
    if usuario_verificado:
        print("Essa conta já existe")
        print(usuarios)
        return
    else:
        user_name = input("Insira ser nome completo:\n")
        user_data_nascimento = input("Insira sua data de nascimento no formato abaixo\ndd-mm-yyyy\n")
        endereco = input("Insira seu indereço no formato abaixo\nlogradouro, nro - bairro - cidade/sigla estado:\n")
        usuarios.append({"Nome":user_name, "Data de nascimento": user_data_nascimento, "Cpf":cpf_usuario, "Endereço": endereco})

def verificar_usuario(cpf):

    for row in usuarios:
        if row["Cpf"] == cpf:
            return row['Cpf'] if row['Cpf'] else None

def criacao_de_contas(numero_conta,agencia,usuarios):
    if len(usuarios) > 0:
        cpf = input('Insira seu CPF:\n')
        # username = input('Insira seu nome completo:\n')
        verificar_usuario(cpf)
        if verificar_usuario:
            print("Conta criada com sucesso!")
            numero_conta += 1
            return {"Agencia":agencia,"Numero da conta":numero_conta,"Usuário":usuarios}
        print("Usuário não encontrado!")
    else:
        print('Você precisa de um usuário para poder criar uma conta')

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        saldo,extrato = deposito(saldo,valor,extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo,extrato = saque(valor = valor,
                              saldo = saldo,
                              limite = limite,
                              numero_saques = numero_saques,
                              LIMITE_SAQUES = LIMITE_SAQUES,
                              extrato = extrato)

    elif opcao == "e":
        extrato_def(extrato,saldo=saldo)
    
    elif opcao == 'c':
        criar_usuario(usuarios)

    elif opcao == 'cc':
        conta = criacao_de_contas(numero_conta,agencia,usuarios)
        if conta:
            conta_corrente.append(conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")