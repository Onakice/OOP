hour1, minute1, hour2, minute2 = [int(i) for i in input().split()]

hours = (hour2 - hour1) * 60
minutes = minute2 - minute1
total_minutes = hours + minutes

#Check Error
if hour1 < 7 or hour2 > 23:
  print("Error")
  exit()
if hour1 == 7 and hour2 == 23:
  if minute2 > 30:
    print("Error")
    exit()
if hour1 == hour2 and minute1 > minute2:
    print("Error")
    exit()
if minute1 >= 60 or minute2 >= 60:
  print("Error")
  exit()

#calculate fee
if total_minutes <= 15:
    print(0)
elif 15 < total_minutes <=180:
    hour = (total_minutes // 60) * 10
    if total_minutes % 60 != 0:
        hour += 10
    print(hour)
elif 180 < total_minutes < 360:
    hour = (total_minutes // 60 - 2) * 20 + 30
    print(hour)
else:
    hour = 200
    print(hour)

#print(total_minutes)