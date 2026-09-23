# Write a program to calculate the difference between two dates

from datetime import datetime

date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Converting string inputs to datetime objects
date1 = datetime.strptime(date1, "%Y-%m-%d")
date2 = datetime.strptime(date2, "%Y-%m-%d")

difference = abs((date2 - date1).days)

print(f"\nDifference between {date1} and {date2} is: {difference} days")
