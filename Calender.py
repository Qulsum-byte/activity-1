import calendar

# Input year and month from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
print("\nCalendar for", calendar.month_name[month], year)
print(calendar.month(year, month))
