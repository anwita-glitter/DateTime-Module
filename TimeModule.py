from datetime import date 
from datetime import time 
from datetime import datetime, timedelta
print(date.today())

d=date(2022,5,11)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d"))

t=time(2,25,47)
print(t.hour)
print(t.strftime("%H:%M:%S"))

full=datetime(2056,1,4,1,45,14)
print(full.strftime("%d-%m-%y %H:%M:%S"))
up_dt=full+timedelta(days=1)
print(up_dt.strftime("%d-%m-%y %H:%M:%S"))
sb_dt=full-timedelta(days=4)
print(sb_dt.strftime("%d-%m-%y %H:%M:%S"))

print(sb_dt>up_dt)