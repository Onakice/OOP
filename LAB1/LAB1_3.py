a, b, c, d = [int(i) for i in input("abcd: ").split()]

hours = (c - a) * 60
minutes = d - b
total_minutes = hours + minutes

if total_minutes < 15:
    print(0)
elif 15 <= total_minutes < 180:
    hour = (total_minutes // 60) * 10
    if total_minutes > 180 :    
        print(hour)
    # if total_minutes % 60 != 0:
    #     hour += 20

elif 180 <= total_minutes < 360:
    hour = (total_minutes // 60) * 20
    # if total_minutes % 60 != 0:
    #     hour += 20
    print(hour)
else:
    hour = 200
    print(hour)

#print(total_minutes)