"""
Assignment - String assignment
"""

days = input("Enter number of days: ")
print(type(days))  # Check the type of days
days = int(days)  # Convert days to integer
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"{days} days are {hours} hours, or {minutes} minutes, or {seconds} seconds.")
