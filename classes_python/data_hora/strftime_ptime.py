from datetime import datetime

def utilizando_strftime():
    data_hora_atual = datetime.now()
    mascara_ptbr = '%d/%m/%Y %a'
    print(data_hora_atual.strftime(mascara_ptbr))
    
# utilizando_strftime()

def utilizando_strptime():
    data_hora_str = '2024-09-24 13:30'
    mascara_en = '%Y-%m-%d %H:%M'
    data_convertida = datetime.strptime(data_hora_str,mascara_en)
    print(data_convertida)
    
# utilizando_strftime()

variavel = 'I-BR-PA-ATM-ATM-HL4-01'
print(variavel.split('-')[2] == 'DF')