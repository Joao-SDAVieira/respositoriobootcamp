from datetime import datetime
data_hora = []
for i in range(15):
    

    data = datetime.now()
    mascara_en = '%d-%m-%Y %H:%M'

    data_formatada = datetime.now().strftime(mascara_en)
    data_hoje = [data[:-6] for data in data_hora if data[:-6] == data_formatada[:-6]]
    # print(data_formatada[:-6])

    if len(data_hoje) <1:
        
        data_hora.append(data_formatada)
        print('Saque realizado com sucesso')
    elif data_hoje.count(data_hoje[-1]) == 10:
        print('Limite de saques atingido')
        
    else:
        print('Saque realizado')
        data_hora.append(data_formatada)        
    # if data_hora[-1] != data_formatada[:-6]:
    #     print('Saque realizado com sucesso!')
    #     print(i)
    #     data_hora.append(data_formatada)
    # else:
    #     print('Você atingiu o limite de saque!')
            

# for i in range (10):
#     if len(data_hora) > 0:
#         for data in data_hora:
#             print(data)
#             if data_formatada[:-6] == data[:-6]:
#                 print('data já informada')
#             else:
#                 data_hora.append(data_formatada)
#     else:
#         print('vazia')
#         data_hora.append(data_formatada)
        
        
# for i in range(12):
#     lista.append(data_formatada)
#     print(data_formatada,type(data_formatada))
#     if data_formatada[:-6] in:
#         print('data já existe')