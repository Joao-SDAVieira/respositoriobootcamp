from datetime import datetime, timezone, timedelta
import pytz

"""Essas são as formas de conseguir a data e hora atual de acordo com a região, no caso do pytz é mais facil e eficiente"""
def utilizando_pytz():
    data = datetime.now(tz=pytz.timezone('Europe/Oslo'))
    print(pytz.timezone('Europe/Oslo'))

utilizando_pytz()

def utilizando_datetime():
    data_oslo = datetime.now(timezone(timedelta(hours=2)))
    data_sp = datetime.now(timezone(timedelta(hours=-3)))
    print(data_oslo,'\n',data_sp)

utilizando_datetime()