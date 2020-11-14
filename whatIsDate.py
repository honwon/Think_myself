import datetime
# pip install python-dateutil
from dateutil.relativedelta import relativedelta

td =datetime.datetime.today()

pd =[
 datetime.date(year=9999,month=12,day=31),
 td.year,
 td.month,
 td.day,
 td.max,
 td.min,
 td.replace(year=2030,month=12),
 datetime.time(hour=23,minute=59,second=59,microsecond=999999),
 datetime.datetime(year=9999, month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
 # beteewn to date, time, or datetime
]
strpd = list(map(str,pd))
print('\n'.join(strpd))
print(str(datetime.date(2002, 12, 4).isoformat()))

print(td)
print(td-relativedelta(years=1,months=1,days=2,minutes=10))
print(td-datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0))
print(datetime.tzinfo())
print(datetime.timezone(datetime.timedelta(hours=9)))
print(datetime.timedelta(hours=1,seconds=59).total_seconds())
print(datetime.date.fromisoformat('2019-12-04'))

print(datetime.datetime.fromisoformat('2011-11-04'))
print('G2Gss')