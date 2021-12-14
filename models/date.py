from datetime import date, datetime

date_today = date.today()
print(date_today)


now = datetime.now()

dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
print("date and time =", dt_string)

dt2_string = now.strftime("%H:%M:%S")
print("time =", dt2_string)
