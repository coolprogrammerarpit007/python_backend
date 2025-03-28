
# Handling Dates and Time in Python

import datetime
date = datetime.date(2025,3,28)
# print(date)

today = datetime.date.today()
# print(f"Today Date: {today}")

# working with time

time = datetime.time(10,0,0)
# print(time)

current_time = datetime.datetime.now()
now = current_time.strftime("%H:%M:%S")
# print(f"current time: {current_time}")
# print(f"current time: {now}")

target_date = datetime.datetime(2030,5,20,12,0,0)
current_time_now = datetime.datetime.now()

# if target_date < current_time_now:
#     print("Targer date has been passed")
# else:
#     print("Not passed yet!")

