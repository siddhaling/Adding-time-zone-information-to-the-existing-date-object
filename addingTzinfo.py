import pandas as pd
from datetime import date 
import pytz


firsDate=date(2020, 11,1)
secondDate=date(2021,11,1)

dates=pd.date_range(firsDate,secondDate, freq='d')

date1=dates[0]
print(date1)

tz=pytz.timezone('Europe/Zurich')

date1_tz=tz.fromutc(date1)
print(date1_tz)

date1_tz1=pytz.utc.localize(date1, is_dst=None).astimezone(tz)
print(date1_tz1)