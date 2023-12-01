# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

miles = 10
time_min = 30
time_sec = 30

km_per_mile = 1.6
sec_per_min = 60
min_per_hr = 60

total_time_min = time_min + time_sec / sec_per_min
total_time_hr = total_time_min / min_per_hr

speed_km_per_hr = miles * km_per_mile / total_time_hr
print("Speed (km/hr): " + str(speed_km_per_hr))