def get_date():
    day = input("Enter the day: ")
    month = input("Enter the month: ")
    year = input("Enter the year: ")
    date = (f"{year}/{month}/{day}")
    return date
date = get_date()
print(date)