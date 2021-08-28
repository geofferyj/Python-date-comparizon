from datetime import datetime, date

import pytz

# Will result in an error
# datetime.datetime.now() >= datetime.date.today()


date1 = date(1995, 3, 20)
date2 = date(2020, 1, 1)
dob_a = datetime(1995, 3, 20)
dob_b = datetime(2020, 1, 1)


print("date1 comes before date2?", date1 < date2)
print("date1 comes after date2?", date1 > date2)
print("date1 is equal to date2?", date1 == date2)


if  dob_a > dob_b:
    print("person a is older than person b")
else:
    print("person b is older than person a")



# Create timezone objects for different parts of the world
tz_ny= pytz.timezone('America/New_York')
tz_lon = pytz.timezone("Europe/London")

# Year, Month, Day, Hour, Minute, Second
date_time = datetime(2010, 4, 20, 23, 30, 0)

# Localize the given date, according to the timezone objects
date_with_timezone_1 = tz_ny.localize(date_time)
date_with_timezone_2 = tz_lon.localize(date_time)

# These are now, effectively no longer the same *date* after being localized
print(date_with_timezone_1) # 2010-04-20 23:30:00-04:00
print(date_with_timezone_2) # 2010-04-20 23:30:00+01:00

print(date_with_timezone_1 == date_with_timezone_2)

tz_ny= pytz.timezone('America/New_York')
tz_l = pytz.timezone("Europe/London")
date_with_timezone = datetime(2010,4,20).astimezone(tz=tz_ny)
date_without_timezone = datetime(2010,4,20).astimezone(tz=tz_l)

print(date_with_timezone == date_without_timezone)
