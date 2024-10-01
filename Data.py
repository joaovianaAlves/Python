from datetime import date, datetime, timedelta

dateFixed = date(2023, 10, 1)
dateToday = date.today()
dateFixedFull = datetime(2023, 10, 23, 10, 0,0)
dateFull = datetime.today()

dateToday = dateToday + timedelta(weeks=4)

print(dateFixed)
print(dateToday)
print(dateFixedFull)
print(dateFull)