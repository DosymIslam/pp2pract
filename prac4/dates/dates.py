# dates.py

from datetime import datetime, timedelta, timezone

# Current date and time
now = datetime.now()
print("Current date:", now)

# Create specific date
specific_date = datetime(2025, 1, 1)
print("Specific date:", specific_date)

# Date formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Time difference
future = now + timedelta(days=10)
difference = future - now
print("Difference in days:", difference.days)

# Timezone example
utc_time = datetime.now(timezone.utc)
print("UTC time:", utc_time)