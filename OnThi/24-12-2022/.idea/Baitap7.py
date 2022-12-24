from datetime import date, datetime, timedelta
date = date.today()
print(date.strftime("%d/%m/%Y"))

# cộng năm
date = date.replace(year=date.year + 5)
print(date.strftime("%d/%m/%Y"))

# công tháng
month = datetime.timedelta(days=30*3)
date = date+month
print(date.strftime("%d/%m/%Y"))



