lista = []
indice = 1

def adicionar(lista):
    item = input('Qual item deseja adicionar?\n->> ')
    lista.append(item)
    
    
def listar(lista):
    for i, item in enumerate(lista):
        print(f'{i+1}. {item}')
        
def excluir(lista):
    item = int(input('Digite o número do item que deseja excluir\n->> '))
    item = item-1
    lista.pop(item)

menu = 'Lista de Compras!\nEscolha\n\n[A]dicionar\n[L]istar\n[E]xcluir\n[S]air'


continuar = True
while continuar:
    try:
        print(menu)
        escolha = input('\nSelecionar: ')

        match escolha.upper():
            case 'A':
                adicionar(lista=lista)
                indice += 1
            case 'L':
                if len(lista) > 0:
                    listar(lista)
                else:
                    print('Sua lista está vazia!')
            case 'E':
                if len(lista) > 0:
                    excluir(lista=lista)
                else:
                    print('Sua lista está vazia!')
            case 'S':
                print('Saindo...')
                break
    except:
        print('Digite um valor válido')