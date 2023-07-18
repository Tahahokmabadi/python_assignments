from datetime import date
from datetime import datetime

day = int(input("Enter your day of birth: "))
month = int(input("Enter your month of birth: "))
year = int(input("Enter your year of birth: "))
today = date.today()
time_in_secends = ((datetime.now() - datetime(year=year, month=month, day=day)).total_seconds()) // 1
print("you are", time_in_secends, "secends old")

time_in_days = ((today.year - year ) * 365 + (today.month - month) * 30 + (today.day - day)) // 1
print("you are", time_in_days, "days old")

time_in_weeks = (time_in_days) // 7
print("you are", time_in_weeks, "weeks old")