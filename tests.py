from datetime import datetime, timedelta, date

now = date.today()
date_str = '2026-04-20'
my_date = datetime.fromisoformat(date_str).date().weekday()
print(my_date)