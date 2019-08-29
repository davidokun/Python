import datetime

# Create a time
t = datetime.time(9, 16, 10)
print(t)

# Get time
print(t.hour)
print(t.minute)
print(t.second)

# Dates
today = datetime.date.today()
print(today)

print(today.timetuple())

# Replace date
d1 = datetime.date(2016, 3, 11)
print(d1)
d2 = d1.replace(year=2018)
print(d2)

# Operations
d1 = datetime.date(1978, 6, 29)
d2 = datetime.date(2018, 6, 29)
print(d2 - d1)
