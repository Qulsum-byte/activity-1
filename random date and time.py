print("random date and time")
import random
from datetime import datetime, timedelta
# Generate a random number of days within a year (365 days)
random_days = random.randint(0, 365)
# Generate a random number of seconds within a day (24 * 60 * 60 seconds)
random_seconds = random.randint(0, 24 * 60 * 60)
# Set the start date (e.g., Jan 1, 2024)
start_date = datetime(2024, 1, 1)
# Add random days and seconds to the start date
random_date_time = start_date + timedelta(days=random_days, seconds=random_seconds)
# Print the random date and time
print("Random Date and Time:", random_date_time)

