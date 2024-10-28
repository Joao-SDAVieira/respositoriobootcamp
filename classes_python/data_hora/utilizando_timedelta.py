from datetime import date, timedelta, datetime, time

from pytz import UTC

tipo_carro = 'P'

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_hora_atual = datetime.now()

print(data_hora_atual)
if tipo_carro == 'P':
    data_estimada = data_hora_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegando ás {data_hora_atual} ficará pronto ás {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_hora_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegando ás {data_hora_atual} ficará pronto ás {data_estimada}')
else:
    data_estimada = data_hora_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegando ás {data_hora_atual} ficará pronto ás {data_estimada}')
    

"""Uma observacao sobre timedelta, é que a operação só funciona com datas, se executar a operação com time por exemplo (apenas
com minutos horas e segundos, não funcionara, como no exemplo a seguir)"""
#funciona pois é um objeto date
print(date.today() - timedelta(days=2))

#não funciona, precisa construir um datetime, passar a data completa, fazer a operação com o timedelta e depois extrair o time apenas
# print(time(10,19,20) - timedelta(hours=1))

#funciona, extraindo apenas a hora de datetime
resultado = datetime(2023,7,25,18,19,22) - timedelta(hours=1)
print(resultado.time())

