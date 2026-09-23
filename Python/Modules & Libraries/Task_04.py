# Use datetime module to display current date and time.

import datetime

current_datetime = datetime.datetime.now()

# Display current date and time
print("Current Date and Time:", current_datetime)
print("Formatted Date       :", current_datetime.strftime("%d-%m-%Y"))
print("Formatted Time       :", current_datetime.strftime("%H:%M:%S"))