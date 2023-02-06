from datetime import datetime 

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
DaysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

year = datetime.today().year
month = Months[datetime.today().month - 1]
day_of_month = datetime.today().strftime("%d")
day_of_week = DaysOfTheWeek[datetime.today().weekday()]

print(f'Today is {day_of_week}, {month} {day_of_month}, {year}')