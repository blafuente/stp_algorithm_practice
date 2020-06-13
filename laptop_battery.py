n = 4
events = [25, -30, 70, -10]
events2 = [10, -20, 61, -15]
case1 = [-10, 60, 10]

battery = 50

for i in case1:
    battery = battery + i
    if battery > 100:
        battery = 100

print(battery)


